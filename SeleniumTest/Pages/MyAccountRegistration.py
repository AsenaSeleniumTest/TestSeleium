from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from Pages.MyAccountPage import MyAccountPage
from Pages.HomePage import HomePage

class MyAccountRegistration(MyAccountPage):
    """ This class contains the locators and methods for the My Account Registration page """
    
    gender_element = (By.NAME,"gender")
    first_name_element = (By.NAME, "firstname")
    last_name_element = (By.NAME, "lastname")
    dob_element = (By.ID, "dob")
    email_element = (By.NAME, "email")
    company_name_element=   (By.NAME, "company")
    street_element = (By.NAME, "street_address")
    suburb_element = (By.NAME, "suburb")
    postcode_element = (By.NAME, "postcode")
    city_element = (By.NAME, "city")
    state_element = (By.NAME, "state")
    country_element = (By.NAME, "country")
    telephone_element = (By.NAME, "telephone")
    fax_element = (By.NAME, "fax")
    news_letter_element = (By.NAME, "newsletter")
    password_element = (By.NAME, "password")
    confirm_password_element = (By.NAME, "confirmation")
    submit_continue_element = (By.XPATH, "//button[@id='tdb4']")
    
    def __init__(self, driver):
        super().__init__(driver)

    def select_gender(self,gender):
        """
        Select the gender radio button  """
        MyAccountPage.click_element(self,element = self.gender_element) 

    def type_first_name(self,first_name):
        """
        Type the first name """
        MyAccountPage.type_text(self,element = self.first_name_element,text = first_name) 

    def type_last_name(self,last_name):
        """
        Type the last name """
        MyAccountPage.type_text(self,element = self.last_name_element,text = last_name) 

    def type_dob(self,dob):
        """
        Type the date of birth """
        MyAccountPage.type_text(self,element = self.dob_element,text = dob)

    def type_email(self,email):
        """
        Type the email address """
        MyAccountPage.type_text(self,element = self.email_element,text = email)

    def type_company_name(self,company_name):
        """
        Type the company name """
        MyAccountPage.type_text(self,element = self.company_name_element,text = company_name)  

    def type_street(self,street):
        """
        Type the street address """
        MyAccountPage.type_text(self,element = self.street_element,text = street)

    def type_suburb(self,suburb):
        """
        Type the suburb """
        MyAccountPage.type_text(self,element = self.suburb_element,text = suburb)

    def type_postcode(self,postcode):
        """
        Type the postcode """
        MyAccountPage.type_text(self,element = self.postcode_element,text = postcode)

    def type_city(self,city):
        """
        Type the city """
        MyAccountPage.type_text(self,element = self.city_element,text = city)

    def type_state(self,state):
        """
        Type the state """
        MyAccountPage.type_text(self,element = self.state_element,text = state)  

    def type_country(self,country):
        """
        Type the country """
        MyAccountPage.type_text(self,element = self.country_element,text = country)

    def type_telephone(self,telephone):
        """
        Type the telephone number """
        MyAccountPage.type_text(self,element = self.telephone_element,text = telephone)

    def type_fax(self,fax):
        """
        Type the fax number """
        MyAccountPage.type_text(self,element = self.fax_element,text = fax)

    def click_news_letter(self,news_letter):
        """
        Click on the news letter checkbox """
        MyAccountPage.click_element(self,element = self.news_letter_element)        
    
    def type_password(self,password):
        """
        Type the password """
        MyAccountPage.type_text(self,element = self.password_element,text = password)

    def type_confirm_password(self,confirm_password):
        """
        Type the confirm password """   
        MyaccountPage.type_text(self,element = self.confirm_password_element,text = confirm_password)    

    def click_continue_submit(self):
        """
        Click on the continue button """
        MyAccountPage.click_element(self,element = self.submit_continue_element)    