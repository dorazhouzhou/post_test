from page.home_page import HomePage
from page.login_page import LoginPage
from page.login_info_page import LogininfoPage
from page.cour_menu_page import  CourMenuPage
from page.post_choose_position_page import  PostChoosePositionPage
from page.post_input_phone_page import PostInputPhonePage
from page.post_scan_exp_id_page import PostScanExpIdPage
from page.post_confirm_page import PostConfirmPage


class Page:
    def __init__(self,driver):
        self.driver = driver

    @property
    def home(self):
        return HomePage(self.driver)

    @property
    def login(self):
        return LoginPage(self.driver)

    @property
    def login_info(self):
        return LogininfoPage(self.driver)

    @property
    def cour_menu(self):
        return CourMenuPage(self.driver)

    @property
    def post_choose_position(self):
        return PostChoosePositionPage(self.driver)

    @property
    def post_input_phone(self):
        return PostInputPhonePage(self.driver)

    @property
    def post_scan_exp_id(self):
        return PostScanExpIdPage(self.driver)

    @property
    def post_confirm(self):
        return PostConfirmPage(self.driver)
