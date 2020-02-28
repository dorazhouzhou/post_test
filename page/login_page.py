from selenium.webdriver.common.by import By
from base.base_action import BaseAction
import allure
import time

class LoginPage(BaseAction):
    #账号登录
    acc_login_btn =  By.ID,"com.sf.module.edms:id/btn_login_input"

    #返回
    rtn_btn =  By.XPATH, "//*[@text='返回']"

    # 点击账号登录
    @allure.step(title="点击账号登录按钮")
    def click_acc_login_btn(self):
        self.click(self.acc_login_btn)
        time.sleep(2)



