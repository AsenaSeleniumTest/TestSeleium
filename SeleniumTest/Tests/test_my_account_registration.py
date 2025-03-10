import pytest
import unittest
from selenium.webdriver.common.by import By
from SeleniumTest.Configurations.TestData import TestData
from SeleniumTest.Pages.HomePage import HomePage
from SeleniumTest.Pages.MyAccountPage import MyAccountPage
from SeleniumTest.Pages.MyAccountRegistration import MyAccountRegistration

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
        my_cuenta_reg