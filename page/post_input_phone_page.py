import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class PostInputPhonePage(BaseAction):#继承基类方法

    # 输入收件人手机号
    input_rcp_phone = By.ID, "com.sf.module.edms:id/et_phone"
    #再次输入收件人手机号
    input_rcp_phone_again = By.ID, "com.sf.module.edms:id/et_phone_02"
    #下一步
    next_step_btn = By.ID, "com.sf.module.edms:id/fragment_layout"

    #温馨提示弹框
    # 已联系,继续投递
    continue_post_btn= By.XPATH, "//*[@text='已联系,继续投递']"

    #取消投递
    cancel_post_btn = By.XPATH, "//*[@text='取消投递']"


    @allure.step(title="输入收件人手机号")
    def post_input_rcp_phone(self,text):
        self.input(self.input_rcp_phone,text)

    @allure.step(title="再次输入收件人手机号")
    def post_input_rcp_phone_again(self, text):
        self.input(self.input_rcp_phone_again, text)

    @allure.step(title="点击下一步")
    def click_next_step_btn(self):
        self.click(self.next_step_btn)

    @allure.step(title="点击已联系,继续投递")
    def click_continue_post_btn(self):
        self.click(self.continue_post_btn)

    @allure.step(title="点击取消投递")
    def click_cancel_post_btn(self):
        self.click(self.cancel_post_btn)