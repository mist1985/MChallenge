from Locators.Locators import Locators
from Pages.BasePage import BasePage

class HomePage (BasePage):

    def click_on_contact (self):
        self.is_visible(Locators.CONTACT_US)
        self.move(Locators.CONTACT_US)
        self.click(Locators.CONTACT_US)

    def enter_name(self):
        self.is_visible(Locators.CONTACT_US_NAME)
        self.contact_type_name(Locators.CONTACT_US_NAME)

    def enter_email(self):
        self.is_visible(Locators.CONTACT_US_EMAIL)
        self.contact_type_email(Locators.CONTACT_US_EMAIL)

    def enter_mobile(self):
        self.is_visible(Locators.CONTACT_US_MOBILE)
        self.contact_type_mobile(Locators.CONTACT_US_MOBILE)

    def enter_subject(self):
        self.is_visible(Locators.CONTACT_US_SUBJECT)
        self.contact_type_subject(Locators.CONTACT_US_SUBJECT)

    def enter_message(self):
        self.is_visible(Locators.CONTACT_US_MESSAGE)
        self.contact_type_message(Locators.CONTACT_US_MESSAGE)

    def send_message(self):
        self.is_visible(Locators.CONTACT_US_SEND)
        self.contact_type_send(Locators.CONTACT_US_SEND)

    def test_email(self):
        self.is_visible(Locators.CONTACT_US_TEST)

    def close(self):
        self.is_visible(Locators.CONTACT_US_CLOSE)
        self.click(Locators.CONTACT_US_CLOSE)

    def click_on_company_button(self):
        #self.is_visible(Locators.COMPANY_BUTTON)
        self.click(Locators.COMPANY_BUTTON)

    def verify_leadership_section(self):
        self.is_visible(Locators.LEADERSHIP_SECTION)
        self.move(Locators.LEADERSHIP_SECTION)

    def click_on_facebook_button(self):
        self.is_visible(Locators.FACEBOOK_BUTTON)
        self.click(Locators.FACEBOOK_BUTTON)

    def verify_facebook_login_logo(self):
        self.is_visible(Locators.FACEBOOK_LOGO)

    def verify_facebook_profile(self):
        self.is_visible(Locators.FACEBOOK_PROFILE)

    def select_location_anywhere(self):
        self.is_visible(Locators.LOCATION_ANYWHERE)
        self.click(Locators.LOCATION_ANYWHERE)

    def click_on_career(self):
        self.is_visible(Locators.CAREERS_BUTTON)
        self.click(Locators.CAREERS_BUTTON)

    def click_open_position(self):
        self.is_visible(Locators.OPEN_POSITIONS)
        self.click(Locators.OPEN_POSITIONS)

    def select_skopje(self):
        self.is_visible(Locators.LOCATION_SKOPJE)
        self.click(Locators.LOCATION_SKOPJE)

    def job_cards(self):
        self.is_visible(Locators.JOB_CARDS)