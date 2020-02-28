from selenium.webdriver.common.by import By
from base.base_action import BaseAction
import allure


class LogininfoPage(BaseAction):
    #手机号码
    phone = By.XPATH,"//*[@text='输入手机号码']"
    #密码
    pwd = By.ID,"com.sf.module.edms:id/et_login_pwd"
    #登录按钮
    login_btn = By.ID,"com.sf.module.edms:id/btn_login"


    # 输入手机号
    @allure.step(title="输入手机号码")
    def input_phone(self,text):
        self.input(self.phone,text)

    # 输入密码
    @allure.step(title="输入密码")
    def input_pwd(self,text):
        self.input(self.pwd,text)

    # 点击登录按钮
    @allure.step(title="点击登录")
    def click_login_btn(self):
        self.click(self.login_btn)