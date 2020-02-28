import allure
import time
from selenium.webdriver.common.by import By
from base.base_action import BaseAction






class HomePage(BaseAction):#继承基类方法
    # 例：“我”按钮
    me_btn = By.ID, "com.yunmall.lc:id/tab_me"

    # 快递员登录
    courier_login_btn = By.XPATH,"//*[@text='快递员登录']"

    #取快递

    #寄快递



    @allure.step(title="点击快递员登录按钮")
    def click_courier_login_btn(self):
        self.click(self.courier_login_btn)



