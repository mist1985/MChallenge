from Pages.HomePage import HomePage
from selenium import webdriver

driver = webdriver.Chrome("C:\Webdrivers\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(2)

def test_Case4():
    driver.get("http://www.musala.com/")

    Careers = HomePage(driver)
    """ Click on Career """
    Careers.click_on_career()

    """ Click on Open Positions """
    Careers.click_open_position()

    """ Click on Skopje """
    Careers.select_skopje()

    """ Print all of the positions """
    for job in driver.find_elements_by_class_name("card-jobsHot"):
        print(job.text)

    driver.quit()

