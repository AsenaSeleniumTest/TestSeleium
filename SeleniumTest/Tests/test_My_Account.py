import pytest
import unittest
from selenium.webdriver.common.by import By
from Configurations.TestData import TestData
from Pages.HomePage import HomePage
from Pages.MyAccountPage import MyAccountPage
import os


class Test_my_account:
    """ This class contains the test cases for the my account page """
    driver = None
    """ Test the my account page of the application """
    @pytest.mark.logintest
    def test_login(self,driver_Setup):
        """Test case to validate login"""
        self.driver = driver_Setup
        self.driver.get(TestData.home_url)
        hp1 = HomePage(self.driver)
        hp1.click_element(hp1.myaccount_link)
        my_cuenta= MyAccountPage(self.driver)
        my_cuenta.type_user("bpb@online.com")
        my_cuenta.type_password("bpb")
        my_cuenta.click_signIn()
        assert my_cuenta.get_title() == "My Account"
    
    @pytest.mark.loginError
    def test_login_error(self,driver_Setup):
        """Test case to validate login error message

        Args:
            driver_setup (_type_): This test is to valida the login error message when the user inputs wrong username
        """
        self.driver = driver_Setup
        self.driver.get(TestData.home_url)
        hp1 = HomePage(self.driver)
        hp1.click_element(hp1.myaccount_link)
        my_cuenta= MyAccountPage(self.driver)
        my_cuenta.type_user(TestData.email)
        my_cuenta.type_password(TestData.password)
        my_cuenta.click_signIn()
        
        assert "Error: No match for E-Mail Address and/or Password." in my_cuenta.get_login_message_error()     