#导入模块
import time  # 时间模块
from selenium.common.exceptions import TimeoutException  # Thrown when a command does not complete in enough time
from selenium.webdriver.common.by import By  # 用By帮助定位元素
from selenium.webdriver.support.wait import WebDriverWait  # 元素等待
from appium import webdriver


# 定义一个类方法---基类，将常用的,重复操作的方法定义到基类中，后续操作可以继承基类的方法，调用想要进行的操作方法，简单快捷
class BaseAction:
    # 初始化方法，后面方法中可以调用driver这个对象
    def __init__(self, driver):
        self.driver = driver

    # 根据特征找一个元素，调用此方法最后会返回到要定位的元素
    def find_element(self, feature, timeout=10, poll=1.0):  # 这里设置了找元素的限制时间10秒，频率Poll设置的1秒
        """
        根据特征，找元素
        feature: 特征
        timeout: 超时时间
        poll: 频率
        return: 元素
        """
        # 为了更加简洁方便，这里是用的By去定位，例：用id属性找元素，driver.find_element_by_id("value")，等价于driver.find_element(By.ID,"value")

        feature_by, feature_value = feature  # 特征属性，特征属性值=该特征   例：feature="By.ID","value"
        element = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(feature_by, feature_value)) # 元素定位，设置了隐式等待
        return element

    # 根据特征找多个符合条件的元素，调用此方法最后会返回一个列表,注释同上
    def find_elements(self, feature, timeout=10, poll=1.0):
        """
        根据特征，找多个符合条件的元素
        feature: 特征
        timeout: 超时时间
        poll: 频率
        return: 元素
        """
        feature_by, feature_value = feature
        element = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(feature_by, feature_value))
        return element

    # 调用此方法，传入特征，做一个点击的动作
    def click(self, feature):
        self.find_element(feature).click()  # 此处调用了查找元素的方法find_element，后面还有很多动作，都调用了查找元素二点方法，后续不再解释

    #有时候有的元素定位不到，模拟手指进行点击屏幕
    def swipe_to_location(self,location):
        self.driver.tap([(847,927)])


    # 调用此方法，在定位到的输入框中，输入文本信息
    def input(self, feature, content):
        self.find_element(feature).send_keys(content)

    # 调用此方法，清除内容
    def clear(self, feature):
        self.find_element(feature).clear()

    # 调用此方法，点击返回
    def press_back(self):
        self.driver.press_keycode(4)

    # 调用此方法，相当于拍了一下回车确认，有时候部分界面没有确认的按钮，输入文本后，可调用此方法
    def press_enter(self):
        self.driver.press_keycode(66)

    # 调用此方法，获取text文本内容
    def get_text(self, feature):
        return self.find_element(feature).text

    # 调用此方法，通过输入"message",判断toast弹框是否存在，若存在返回True,不存在则返回False
    def is_toast_exist(self,message):  # 此处的message是输入弹框中提示的内容，部分或完整的都可以

        message_text = By.XPATH, "//*[contains(@text,'%s')]" % message  # toast提示信息的特征
        try:
            self.find_element(message_text, 5, 0.1)
            return True
        except TimeoutException:
            return False

    # 调用此方法,可以根据部分内容获取toast弹框上的所有内容，一般做断言的时候会用到
    def get_toast_text(self, message):
        if self.is_toast_exist(message):  # 这里先做了一个判断，如果弹框存在我们才能获取对应的toast内容
            message_xpath = By.XPATH,"//*[contains(@text,'%s')]" % message
            return self.find_element(message_xpath, 5, 0.1).text
        else:  # 若未定位到弹框，我们可以设置一个抛出异常的提示，提示"toast未出现，请检查"
            raise Exception("toast未出现，请检查")

    # 调用此方法，传入元素特征，判断我们定位的元素是否存在，存在返回True,不存在返回False，这个方法也是在断言的时候用得比较多哦！！！
    def is_feature_exist(self, feature):
        try:
            self.find_element(feature)
            return True
        except TimeoutException:
            return False

    #  此处封装了滑动一次屏幕的方法
    def scroll_page_one_time(self, direction="up"):  # 传入想要操作的一个方向，此处以向上滑动为例，将参数"up"传入
        # direction:up/down/left/right,根据实际情况选择方向

        # 由于不同的系统可能屏幕宽高不一样，下面我们就先获取整个屏幕的宽高尺寸来确定我们滑动的点
        width = self.driver.get_window_size()["width"]  # 获取屏幕的宽
        height = self.driver.get_window_size()["height"]  # 获取屏幕的高

        center_x = width / 2  # 此处是X轴（横向）的中点
        center_y = height / 2  # 此处是Y轴（纵向）的中点

        # 确定一个“上点”坐标位置，相当于手指在横向的中间，并离上边1/4处，选择1/4处比较保险，以免上边界有遮挡，此处做解释，后面其他3个点同理
        top_x = center_x
        top_y = height / 4 * 1

        # 确定一个“下点”坐标位置
        bottom_x = center_x
        bottom_y = height / 4 * 3

        # 确定一个“左点”坐标位置
        left_x = width / 4 * 1
        left_y = center_y

        # 确定一个“右点”坐标位置
        right_x = width / 4 * 3
        right_y = center_y

        # 往上滑动（由"下点坐标位置"往"上点坐标位置"滑动）
        if direction == "up":  # 根据传入的参数，进行对应的操作
            self.driver.swipe(bottom_x, bottom_y, top_x, top_y, 3000)  # #此处是2个点的坐标，“3000”毫秒是滑动的时间，大家可以自己设置感受一下哈滑动的速度

        # 往下滑动（由"上点坐标位置"往"下点坐标位置"滑动）
        elif direction == "down":
            self.driver.swipe(top_x, top_y, bottom_x, bottom_y, 3000)

        # 往左滑动（由"右点坐标位置"往"左点坐标位置"滑动）
        elif direction == "left":
            self.driver.swipe(right_x, right_y, left_x, left_y, 3000)

        # 往右滑动（由"下点坐标位置"往"上点坐标位置"滑动）
        elif direction == "right":
            self.driver.swipe(left_x, left_y, right_x, right_y, 3000)

        #  若运行出错，可设置抛出一个异常提醒，检查方向参数是否写错
        else:
            raise Exception("请检查参数是否正确，up/down/left/right")

    # 封装一个边滑动屏幕边找元素的方法，因为有时候要定位的元素需要滑动屏幕才能看到，传入元素特征，以及滑动方向的参数，最后定位元素
    def find_element_with_scroll(self, feature, direction="up"):
        page_source = self.driver.page_source  # 获取当前的页面源码，每个页面只有一个page_source
        while True:

            try:  # 在当前页面定位元素，若找到该元素，则返回该元素
                element = self.find_element(feature)
                return element

            except Exception:  # 若在当前页面未定位到元素，则滑动一次屏幕
                self.scroll_page_one_time(direction)  # 若在当前页面未定位到元素，此处就调滑动一次屏幕的方法，滑动屏幕后再定位元素
                if self.driver.page_source == page_source:  # 滑动屏幕后，我们要先做个小判断，看页面是否真的滑动了，这就要看页面源码是否和刚开始一样
                    print("亲，还在滑？已经到底啦！！！")   # 如果2次的page_source一样，那就提示已经到底部了
                    break  # 结束，不会继续执行了
                # 如果此次和上次的page_source不一样，证明屏幕滑动了，可以继续循环执行try,找元素 。 注意：记得获取此次的新页面源码page_source，方便下一次的判断
                page_source = self.driver.page_source

    # 此方法用来判断关键字是否在当前页面出现
    def is_keyword_in_page_source(self, keyword, timeout=10, poll=0.1):

        end_time = time.time() + timeout  # 结束时间= 当前时间+设置的时间段，此处设置了一个10秒的查找时间
        while True:
            if end_time < time.time():  # 如果结束时间>当前执行时间，返回False，此处的意义是想给页面最多10秒的加载查找时间，超过这个时间没找到，证明当前页面没有此元素
                return False
            if keyword in self.driver.page_source:  # 如果关键字在当前页面，返回True
                return True

            time.sleep(poll)