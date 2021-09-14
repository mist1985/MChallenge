import csv
import pandas as pd
from pandas import DataFrame as df
import requests
import time
from Pages.BasePage import BasePage
from Pages.HomePage import HomePage
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pytest


driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                                   desired_capabilities=DesiredCapabilities.CHROME)


#driver = webdriver.Chrome("C:\Webdrivers\chromedriver.exe")
#driver.maximize_window()
#driver.implicitly_wait(2)

driver.get("http://www.musala.com/")

def test_Case1():
    #There is also a CSV file, but I have chosen to use the XLSX file

    df = pd.read_excel(r'C:\Users\MIHAJLO\PycharmProjects\MihajloS\XLS_Mihajlo.xlsx')

    #Iteration counter
    i = 0
    #Counter for excel file rows for the emails
    a = 0
    while i < 5:
        a <= 5
        email = df.email
        contact_email = driver.find_element_by_xpath("//input[@id='cf-2']")

        contact_Us = HomePage(driver)
        contact_Us.click_on_contact()
        contact_Us.enter_name()
        contact_email.clear()
        contact_email.send_keys(email[a])
        contact_Us.enter_mobile()
        contact_Us.enter_subject()
        contact_Us.enter_message()
        contact_Us.send_message()

        #Verify that the The e-mail address entered is invalid appears
        try:
            contact_Us.test_email()
            contact_Us.close()

        except:
            print("There is no warning about an invalid email address!")
            break
        #Increment email row
        a += 1
        #Increment loop
        i += 1
    driver.quit()