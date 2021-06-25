from selenium.webdriver.common.by import By


class Locators:

    #Home Page Locators

    #Contact Us Locator
    CONTACT_US=(By.CSS_SELECTOR,"section.contacts:nth-child(3) div.inner-wraper div.contacts-title:nth-child(1) div.links-buttons:nth-child(2) a.fancybox:nth-child(1) button.contact-label.btn.btn-1b > span:nth-child(1)")

    #Contact Us Name
    CONTACT_US_NAME = (By.XPATH,"//input[@id='cf-1']")

    #Contact Us Email
    CONTACT_US_EMAIL = (By.XPATH,"//input[@id='cf-2']")

    #Contact Us Mobile
    CONTACT_US_MOBILE = (By.CSS_SELECTOR,"#cf-3")

    #Contact Us Subject
    CONTACT_US_SUBJECT = (By.XPATH,"//input[@id='cf-4']")

    #Contact Us Your Message
    CONTACT_US_MESSAGE = (By.CSS_SELECTOR,"#cf-5")

    #Send Button Contact US
    CONTACT_US_SEND = (By.XPATH,"//body/div[@id='fancybox-wrap']/div[@id='fancybox-outer']/div[@id='fancybox-content']/div[1]/div[1]/div[1]/form[1]/div[3]/p[1]/input[1]")

    #Not a Robot
    CONTACT_US_ROBOT = (By.XPATH,"//body/div[@id='fancybox-wrap']/div[@id='fancybox-outer']/div[@id='fancybox-content']/div[1]/div[1]/div[1]/form[1]/div[3]/p[1]/input[1]")

    #Close
    CONTACT_US_CLOSE = (By.XPATH,"//a[@id='fancybox-close']")

    #Test
    CONTACT_US_TEST =(By.XPATH,"//span[contains(text(),'The e-mail address entered is invalid.')]")

    #Company Button
    COMPANY_BUTTON = (By.CSS_SELECTOR,"div:nth-child(1) div.menu-main-nav-container ul.nav li.menu-item.menu-item-type-post_type.menu-item-object-page.menu-item-887:nth-child(1) > a.main-link")

    #Leadership section
    LEADERSHIP_SECTION = (By.XPATH, "//body/main[@id='company']/div[@id='primary']/div[@id='content']/div[2]/section[3]")

    #Facebook Button
    FACEBOOK_BUTTON = (By.XPATH, "//body/footer[1]/div[1]/div[1]/a[4]/span[1]")

    #Facebook Profile
    FACEBOOK_PROFILE = (By.ID, "//body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]")

    #Careers button
    CAREERS_BUTTON = (By.XPATH,"//body[1]/header[1]/nav[2]/div[1]/div[1]/ul[1]/li[5]/a[1]")

    #Open Positions
    OPEN_POSITIONS = (By.XPATH,"//body[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/a[1]/button[1]/span[1]")

    #Location Anywhere
    LOCATION_ANYWHERE = (By.XPATH, "//option[contains(text(),'Anywhere')]")

    #Location Skopje
    LOCATION_SKOPJE = (By.XPATH, "//option[contains(text(),'Skopje')]")

    #Location Log
    LOCATION_LOG = (By.CSS_SELECTOR, "div.content-area:nth-child(1) div.site-content section.join-us div.inner-wraper article.card-jobsHot:nth-child(2) div.card-container.applyflip a.card-jobsHot__link div.card div.front > p.card-jobsHot__location")

    #Facebook Login Logo
    FACEBOOK_LOGO = (By.XPATH,"//body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/img[1]")

    #Job Cards
    JOB_CARDS = (By.CLASS_NAME,"card-jobsHot")
