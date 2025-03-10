from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from SeleniumTest.Pages.MyAccountPage import MyAccountPage

class MyAccountRegistration(MyAccountPage):
    """ This class contains the locators and methods for the My Account Registration page """
    gender_element = (By.NAME,"gender")
    first_name_element = (By.ID, "firstname")
    last_name_element = (By.ID, "lastname")
    dob_element = (By.ID, "dob")
    email_element = (By.ID, "email")
    company_name_element=   (By.NAME, "company")
    street_element = (By.ID, "street_address")
    suburb_element = (By.ID, "suburb")
    postcode_element = (By.ID, "postcode")
    city_element = (By.ID, "city")
    telephone_element = (By.ID, "telephone")
    fax_element = (By.ID, "fax")
   
  
    
