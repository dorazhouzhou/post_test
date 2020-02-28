import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class PostConfirmPage(BaseAction):#继承基类方法

    # 已投递
    hv_post_btn = By.XPATH,"//*[@text='已投递']"
    #未开门
    not_open_btn = By.XPATH, "//*[@text='未开门']"


    @allure.step(title="点击已投递")
    def click_hv_post_btn(self):
        self.click(self.hv_post_btn)

    @allure.step(title="点击未开门")
    def click_not_open_btn(self):
        self.click(self.not_open_btn)