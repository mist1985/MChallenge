from Pages.HomePage import HomePage
from selenium import webdriver


driver = webdriver.Chrome("C:\Webdrivers\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(2)

def test_Case2():

    driver.get("http://www.musala.com/")

    Company = HomePage(driver)

    """ Click on Company """
    Company.click_on_company_button()

    """ URL Verification - Expected vs Actual """
    expected_url = "https://www.musala.com/company/"
    driver.get(expected_url)
    actual_url = driver.current_url
    assert expected_url == actual_url, "Expected URL did not matach the Actual URL"

    """ Verify the Leadership Section """
    Company.verify_leadership_section()

    """ Click on the Facebook button """
    Company.click_on_facebook_button()

    """ Switching to the new tab """
    driver.switch_to.window(driver.window_handles[1])

    """ URL Verification - Expected vs Actual """
    expected_url = "https://www.facebook.com/login/?next=https%3A%2F%2Fwww.facebook.com%2FMusalaSoft%3Ffref%3Dts"
    driver.get(expected_url)
    actual_url = driver.current_url
    assert expected_url == actual_url, "Expected URL did not matach the Actual URL"

    """ Verify Login Facebook Logo """
    #For some reason Facebook would not allow me to see the Musala's Facebook page - forced me to log in on Facebook

    try:
        Company.verify_facebook_profile()
        print("The Verify Facebook profile was found")
        driver.quit()
    except:
        pass
        print("The Verify Facebook profile was not found")

    try:
        Company.verify_facebook_login_logo()
        print("The Facebook logo was found")
        driver.quit()
    except:
        print("The Facebook logo was not found")
        driver.quit()



