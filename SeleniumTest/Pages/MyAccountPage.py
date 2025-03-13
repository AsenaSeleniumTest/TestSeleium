from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.HomePage import HomePage

class MyAccountPage(HomePage):
    new_customer = (By.XPATH, "//h2[contains(text(),'Continue')]")
    returning_customer = (By.XPATH, "//h2[contains(text(),'Returning Customer')]")
    email_address = (By.ID, "email_address")
    password = (By.ID, "password")
    login_button = (By.ID, "tdb5")
    forgot_password = (By.LINK_TEXT, "Password forgotten? Click here.")
    continue_registration_button = (By.ID, "tdb4")
    login_error_element =(By.XPATH,"//td[@class='messageStackError']")
   
    def __init__(self, driver):
        super().__init__(driver)
        
    def type_user(self,username):
        """ Type the email address """
        HomePage.type_text(self,element = self.email_address,text = username)
    
    def type_password(self,passwd):
        """ Type the password """
        HomePage.type_text(self,element = self.password,text = passwd)
    
    def click_signIn(self):
        """ Click on the login button """
        HomePage.click_element(self,element = self.login_button)    
    
    def click_continue_to_registration(self):
        """ Click on the continue button """
        HomePage.click_element(self,element = self.new_customer)
    
    def get_login_message_error(self):
        """ Get the login error message """
        return HomePage.get_element_text(self,element = self.login_error_element)    
        