from selenium.common.exceptions import ElementNotInteractableException
from Pages.HomePage import HomePage as hp
import pytest
import unittest
import sys  
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class Test_BasePage:
    """ Test the base page of the application """
    driver = None
    home_url = "https://practice.bpbonline.com/"
    
    @pytest.mark.hometitle ##this is to run before /after every test 
    def test_setup(self,driver_Setup):
        """ Test main page  the driver for the test """
        self.driver = driver_Setup
        assert self.driver.title == "BPB Online"
        
    @pytest.mark.logintest    
    def test_base_page(self,driver_Setup):
        """ Test the base page of the application """
        self.driver = driver_Setup
        hp1 = hp(self.driver)
                
        hp1.click_element(hp1.myaccount_link)                            
        assert hp1.get_title() == "BPB Online"
    
    @pytest.mark.opennewaccountpage
    def test_new_account_page(self,driver_Setup):
        pass
        
        
               
    @pytest.mark.closedriver
    def tearDown(self):
        """ Test the teardown of the driver """
        self.driver.quit()