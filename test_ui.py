import requests
from selene import browser, have
from selene.support.shared.jquery_style import s, ss
import time
from allure_commons._allure import step

LOGIN = "example1200@example.com"
PASSWORD = "123456"
WEB_URL = "https://demowebshop.tricentis.com/"
API_URL = "https://demowebshop.tricentis.com/"


def test_login():
    with step("Open login page"):
        browser.open("http://demowebshop.tricentis.com/login")
    with step("Fill login form"):
        s("#Email").send_keys(LOGIN)
        s("#Password").send_keys(PASSWORD).press_enter()
    with step("Verify successful authorization"):
        s(".account").should(have.text(LOGIN))


def test_login_with_api():
    responce = requests.post(
        API_URL + "login",
        data={'Email': LOGIN, 'Password': PASSWORD, 'RememberMe': True},
        allow_redirects=False,
    )
    print(responce.text)
    assert responce.status_code == 302
    print(responce.cookies.get("NOPCOMMERCE.AUTH"))
    cookie = responce.cookies.get("NOPCOMMERCE.AUTH")

    with step("Open login page"):
        browser.open(WEB_URL)
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
        browser.open(WEB_URL)
        time.sleep(5)
        s(".account").should(have.text(LOGIN))
    # with step("Fill login form"):
    #     s("#Email").send_keys(LOGIN)
    #     s("#Password").send_keys(PASSWORD).press_enter()
    # with step("Verify successful authorization"):
    #     s(".account").should(have.text(LOGIN))
