from time import sleep

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

caps = {}
caps["platformName"] = "Android"
caps[
    "appium:app"
] = "/Users/jodythomas/projects/appium_py/apk/com.zure.stockzure-30600.apk"
caps["appium:deviceName"] = "Nexus5"
caps["appium:deviceOrientation"] = "portrait"
caps["appium:automationName"] = "UiAutomator2"

url = "http://localhost:4723"


@pytest.fixture(scope="function")
def driver_setup_teardown():
    options = UiAutomator2Options()
    options.load_capabilities(caps)
    driver = webdriver.Remote(url, options=options)
    yield driver
    if driver:
        driver.quit()


def test_login_failed(driver_setup_teardown):
    driver = driver_setup_teardown
    btn_login = driver.find_element(
        by=AppiumBy.XPATH,
        value='//android.view.View[@content-desc="Login click to expand contents"]/android.widget.TextView[2]',
    )
    btn_login.click()

    emailField = driver.find_element(
        by=AppiumBy.XPATH,
        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[2]/android.widget.EditText",
    )
    passWordField = driver.find_element(
        by=AppiumBy.XPATH,
        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View[2]/android.widget.EditText",
    )

    emailField.send_keys("jodythomas@gmai.com")
    passWordField.send_keys("password")

    login_submit = driver.find_element(
        by=AppiumBy.XPATH,
        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View[4]/android.view.View[2]/android.view.View/android.view.View/android.view.View[2]",
    )

    login_submit.click()

    sleep(2)

    error_text = driver.find_element(
        by=AppiumBy.XPATH,
        value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[3]/android.widget.TextView[2]",
    )

    assert (
        error_text.text
        == "Invalid E-Mail Address or Password, you can reset your password on the login screen..."
    )

    sleep(2)
