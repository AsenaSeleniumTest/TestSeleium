import json
import os
class TestData:
    """ This class contains the test data for the application """
    
    def __init__(self):
        self.home_url = "http://automationpractice.com/index.php"
        self.myaccount_link = "http://automationpractice.com/index.php?controller=my-account"
        self.email = "bpb@online.com"
        self.password = "bpb"
        self.data_file="SeleniumTest/TestData/Registrationdata.json"
        

    def read_data_registration(self, file_path):
        """ Read the data from the json file """
        try:
            with open(file_path) as file:
                data = json.load(file)
            return data
        except FileNotFoundError as ex:
            print(f"File not found : {ex.__str__()}")
        return data

    def SeeData(self):
        data = self.read_data_registration(self.data_file)
        print(data)

    def system_info(self):
        """ Get the system information """
        return os.environ   


