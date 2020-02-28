import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction
# 切换钱包：切换钱包
# 格口：Z0001

class PostScanExpIdPage(BaseAction):#继承基类方法

    # 请输入快递运单号
    input_exp_id = By.XPATH,"//*[@text='请输入快递运单号']"

    #完成
    finish_btn = By.ID, "com.sf.module.edms:id/btn_confim"

    @allure.step(title="请输入快递运单号")
    def post_input_exp_id(self,text):
        self.input(self.input_exp_id,text)

    @allure.step(title="完成")
    def click_finish_btn(self):
        self.click(self.finish_btn)