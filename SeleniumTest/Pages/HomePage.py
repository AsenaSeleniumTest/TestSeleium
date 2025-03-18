from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    """ Home page class for the application 
    references: https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.by.html
    """
    home_url = "https://practice.bpbonline.com/"
    welcome_title = (By.XPATH,"//h1[contains(text(),'Welcome to BPB Online')]")
    myaccount_link = (By.LINK_TEXT, "My Account")
    checkout_link = (By.LINK_TEXT, "Checkout")
    cart_content = (By.XPATH, "//div[@id='headerShortcuts']//span[contains(text(),'Cart Contents')]")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def get_title(self):
        """ Get the title of the page """
        return self.driver.title

    def get_url(self):
        """ Get the URL of the page """
        return self.driver.current_url
       
    ## Methods that will be inherited by other pages for common actions like click, wait for element, type text etc
    def click_element(self,element):
        """ Click on the element """
        try:
            self.wait.until(EC.visibility_of_element_located(element)).click()
        except ElementClickInterceptedException as ex:
            print("Element is not clickable : {ex.__str__()}")

    def wait_for_element(self,element):
        """ Wait for the element to be visible """

        return self.wait.until(EC.visibility_of_element_located(element))
    def type_text(self,element,text):
        """ Type text in the element """
        try:
            self.wait.until(EC.visibility_of_element_located(element)).send_keys(text)
        except ElementNotInteractableException:
            print("Element is not interactable") 

    def get_element_text(self,element):
        """ Get the text of an  element on the webpage"""
        return self.wait.until(EC.visibility_of_element_located(element)).text

    def get_element_list(self,element):
        """ Get the list of elements on the webpage"""
        return self.wait.until(EC.visibility_of_all_elements_located(element))
    
    def element_status_enabled(self,element):
        """ Check if the element is displayed on the webpage returns True if enabled """
        return self.wait.until(EC.visibility_of_element_located(element)).is_enabled()

    def element_status_displayed(self,element):
        """ Check if the element is displayed on the webpage  returns True if displayed """
        try:
            return self.wait.until(EC.visibility_of_element_located(element)).is_displayed()
        except NoSuchElementException as ex:
            print("Element not found")
            return ex   
    
    
    
    
"""if __name__ == "__main__":
    pass    """    