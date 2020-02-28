# 导入模块
from appium import webdriver

# 定义一个启动移动端的方法，调用此方法，可以启动指定的APP

def init_driver(no_reset=True):
    desired_caps = dict()
    # 设备信息
    desired_caps['platformName'] = 'Android'#系统名--android的apk还是IOS的ipa
    desired_caps['platformVersion'] = '4.4'#系统版本号
    desired_caps['deviceName'] = '192.168.174.101:5555'#设备号,模拟器的号码，通过adb devices命令查看

    # app信息
    desired_caps['appPackage'] = 'com.sf.module.edms'#apk包名---要启动的app名称
    desired_caps['appActivity'] = '.hibox.ui.entry.EntryActivity'
    desired_caps['unicodeKeyboard'] = True  # 使用unicodeKeyboard的编码方式来发送字符串
    desired_caps['resetKeyboard'] = False  # # 将键盘给隐藏起来

    # 不重置应用
    desired_caps['noReset'] = no_reset

    # Appium 服务器初始化参数之一automationName（自动化测试的引擎），如果不指定时，默认的为UiAutomator1，UiAutomator1
    # 不支持toast的获取。这样在获取toast时，需要指定desired_caps["automationName"] = "UiAutomator2"，
    # desired_caps['automationName'] = 'Uiautomator2'

    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)#启动服务器地址，后面跟的是手机信息

