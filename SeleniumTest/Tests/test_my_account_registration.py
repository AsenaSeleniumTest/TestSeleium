import pytest
import unittest
from selenium.webdriver.common.by import By
from Configurations.TestData import TestData
from Pages.HomePage import HomePage
from Pages.MyAccountPage import MyAccountPage
from Pages.MyAccountRegistration import MyAccountRegistration

class Test_My_Account_Registration:
    """ This class contains the test cases for the my account registration page """
    driver = None
    """ Test the my account registration page of the application """
    @pytest.mark.registration
    def test_registration(self,driver_Setup):
        """Test case to validate registration"""

        self.driver = driver_Setup
        self.driver.get(TestData.home_url)
        hp1 = HomePage(self.driver)
        hp1.click_element(hp1.myaccount_link)
        my_cuenta= MyAccountPage(self.driver)
        my_cuenta.click_continue_to_registration()
        my_cuenta_reg = MyAccountRegistration(self.driver)
        my_cuenta_reg.select_gender(gender)
        my_cuenta_reg.type_first_name(first_name)
        my_cuenta_reg.type_last_name(last_name) 
        my_cuenta_reg.type_dob(dob)
        my_cuenta_reg.type_email(email)
        my_cuenta_reg.type_company_name(company_name)
        my_cuenta_reg.type_street(street)
        my_cuenta_reg.type_suburb(suburb)
        my_cuenta_reg.type_postcode(postcode)
        my_cuenta_reg.type_city(city)
        my_cuenta_reg.type_state(state)
        my_cuenta_reg.type_country(country)
        my_cuenta_reg.type_telephone(telephone)
        my_cuenta_reg.type_fax(fax)
        my_cuenta_reg.click_news_letter(news_letter)
        my_cuenta_reg.type_password(password)
        my_cuenta_reg.type_confirm_password(confirm_password)
        my_cuenta_reg.click_continue_submit()
        TestData.SeeData()
        assert my_cuenta_reg.get_title() == TestData.my_account_title