import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction
# 切换钱包：切换钱包
# 格口：Z0001

class PostChoosePositionPage(BaseAction):#继承基类方法

    # 选择格口
    room_position_btn = By.XPATH,"//*[@text='Z0001']"
    #切换钱包
    change_biil_way_btn = By.XPATH,"//*[@text='切换钱包']"


    @allure.step(title="选择格口")
    def click_room_position_btn(self):
        self.click(self.room_position_btn)

    @allure.step(title="切换钱包")
    def click_change_biil_way_btn(self):
        self.click(self.change_biil_way_btn)