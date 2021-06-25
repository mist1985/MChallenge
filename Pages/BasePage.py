from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class BasePage():

    #This function is called every time a new object of the base class is created
    def __init__(self,driver):
        self.driver = driver

    #This function performs a click on the web element who locator is passed to it and the element is present
    def click(self,by_locator):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_locator)).click()

    def move(self,by_locator):
        element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(by_locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()


    #This function returns Boolean whether an element is visible or not
    def is_visible(self,by_locator):
        element = WebDriverWait(self.driver,5).until(EC.presence_of_element_located(by_locator))
        return bool(element)

    def contact_type_name(self,by_locator):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(by_locator)).clear()
        WebDriverWait(self.driver,5).until(EC.presence_of_element_located(by_locator)).send_keys("Mihajlo Stojanovski")

    def contact_type_email(self,by_locator):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(by_locator)).clear()

    def contact_type_mobile(self,by_locator):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(by_locator)).clear()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(by_locator)).send_keys("38970777019")

    def contact_type_subject(self,by_locator):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(by_locator)).clear()
        WebDriverWait(self.driver,5).until(EC.presence_of_element_located(by_locator)).send_keys("Mihajlo Stojanovski Test")

    def contact_type_message(self,by_locator):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(by_locator)).clear()
        WebDriverWait(self.driver,5).until(EC.presence_of_element_located(by_locator)).send_keys("This is a test")

    def contact_type_send(self,by_locator):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(by_locator)).click()






