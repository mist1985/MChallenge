from Pages.HomePage import HomePage
from selenium import webdriver


driver = webdriver.Chrome("C:\Webdrivers\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(2)

def test_Case3():
    driver.get("http://www.musala.com/")

    Careers = HomePage(driver)

    """Click on the Career button"""
    Careers.click_on_career()

    """Click on Open Positions"""
    Careers.click_open_position()

    """ URL Verification - Expected vs Actual """
    expected_url = "https://www.musala.com/careers/join-us/"
    driver.get(expected_url)
    actual_url = driver.current_url
    assert expected_url == actual_url, "Expected URL did not matach the Actual URL"

    """ Select Location - Anywhere"""
    Careers.select_location_anywhere()
    driver.quit()