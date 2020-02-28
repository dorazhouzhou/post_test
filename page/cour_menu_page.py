# 登录：com.sf.module.edms:id/tv_post_tips
# 我的派件：com.sf.module.edms:id/iv_i_post
# 退出：com.sf.module.edms:id/title_back


import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class CourMenuPage(BaseAction):#继承基类方法
    #角色选择
    choose_role = By.XPATH, "//*[@text='角色选择']"
    #快递员
    courier_role = By.XPATH, "//*[@resource-id='com.sf.module.edms:id/authority_recyclerview']/android.widget.LinearLayout[1]/android.widget.ImageView[1]"
    #样品分发员
    sample_role = By.XPATH, "//*[@resource-id='com.sf.module.edms:id/authority_recyclerview']/android.widget.LinearLayout[2]/android.widget.ImageView[1]"
    #派件
    post_btn = By.XPATH,"//*[@text='派件']"
    #我的派件
    my_post_btn = By.ID, "com.sf.module.edms:id/iv_i_post"
    #退出
    bk_btn = By.ID,"com.sf.module.edms: id / title_back"


    #登录快递员账号后，进入快递员主页分2种情况：1.进入【角色选择】页面再进入快递员【派件】主页；2.跳过【角色选择】直接进入快递员【派件】主页
    #如下需要进行一个判断，当账号登录后，判断当前页面是否有关键字【角色选择】
    @allure.step(title="判断当前页面是否有关键字【角色选择】,有则点击【快递员】")
    def if_role_exist(self):
        if self.is_feature_exist(self.choose_role):
            self.click(self.courier_role)

    @allure.step(title="点击派件按钮")
    def click_post_btn(self):
        self.click(self.post_btn)

    @allure.step(title="点击我的派件按钮")
    def click_my_post_btn(self):
        self.click(self.my_post_btn)