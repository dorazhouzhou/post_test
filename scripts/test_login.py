# 导入模块
import time
import pytest
from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page_entry import Page

# 登录测试类
class TestLogin:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):  #  后置处理方法，用例执行结束自动执行此处的方法，如：用例执行完毕后自动退出
        time.sleep(5)
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_file("login_data.yaml", "test_login")) # 此处是引用了参数化，调用data数据
    def test_login(self,args):

        phone_num = args["phone"]
        pwd = args["pwd"]
        # toast = args["toast"]

        #进入登陆页面
        #1.点击快递员登录
        self.page.home.click_courier_login_btn()
        time.sleep(3)
        #点击账号登录
        self.page.login.click_acc_login_btn()
        #输入手机号
        self.page.login_info.input_phone(phone_num)
        #输入密码
        self.page.login_info.input_pwd(pwd)
        #点击登录
        self.page.login_info.click_login_btn()
        time.sleep(2)
        #判断当前页面是否有关键字【角色选择】,有则点击【快递员】
        self.page.cour_menu.if_role_exist()





        # # 打印提示信息的文本内容
        # message = self.driver.find_element_by_id("com.sf.module.edms:id/dialog_content").text
        # print("message={}".format(message)) # 打印页面出现的提示内容
        #
        # #断言页面是否有提示“抱歉，当前遇到了点问题，你可以稍后再试"，若断言成功，用例通过
        # assert self.page.login.is_toast_exist(toast)



