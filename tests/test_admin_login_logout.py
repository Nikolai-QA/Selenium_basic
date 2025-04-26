from page_object.login_admin import Login
from page_object.logout_admin import Logout



def test_admin_login_logout(browser):
    login = Login(browser)
    logout = Logout(browser)
    login.open()
    login.login_admin()
    logout.logout()