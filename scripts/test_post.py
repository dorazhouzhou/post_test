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
        time.sleep(7)
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_file("exp_id_data.yaml", "test_post")) # 此处是引用了参数化，调用data数据
    def test_post(self,args):

        phone_num = args["phone"]
        pwd = args["pwd"]
        express_id = args["express_id"]
        rcp_phone = args["rcp_phone"]
        rcp_phone_confirm = args["rcp_phone_confirm"]

        # toast = args["toast"]

        # 进入首页
        # 1.快递员登录
        self.page.home.click_courier_login_btn()
        time.sleep(3)
        # 点击账号登录
        self.page.login.click_acc_login_btn()
        # 输入手机号
        self.page.login_info.input_phone(phone_num)
        # 输入密码
        self.page.login_info.input_pwd(pwd)
        # 点击登录
        self.page.login_info.click_login_btn()
        time.sleep(2)
        self.page.cour_menu.if_role_exist()

        # 2.快递员派件
        self.page.cour_menu.if_role_exist()
        #点击派件按钮
        self.page.cour_menu.click_post_btn()
        #选择格口
        self.page.post_choose_position.click_room_position_btn()
        #请输入快递运单号
        self.page.post_scan_exp_id.post_input_exp_id(express_id)
        time.sleep(3)
        #点击完成
        self.page.post_scan_exp_id.click_finish_btn()
        time.sleep(3)
        #输入收件人手机号
        self.page.post_input_phone.post_input_rcp_phone(rcp_phone)
        #再次输入收件人手机号
        self.page.post_input_phone.post_input_rcp_phone_again(rcp_phone_confirm)
        #点击下一步
        self.page.post_input_phone.click_next_step_btn()
        time.sleep(2)
        #点击已投递
        self.page.post_confirm.click_hv_post_btn()







        # # 打印提示信息的文本内容
        # message = self.driver.find_element_by_id("com.sf.module.edms:id/dialog_content").text
        # print("message={}".format(message)) # 打印页面出现的提示内容
        #
        # #断言页面是否有提示“抱歉，当前遇到了点问题，你可以稍后再试"，若断言成功，用例通过
        # assert self.page.login.is_toast_exist(toast)

