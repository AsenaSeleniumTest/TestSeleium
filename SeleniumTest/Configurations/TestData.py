import json
class TestData:
    """ This class contains the test data for the application """
    home_url = "http://automationpractice.com/index.php"
    myaccount_link = "http://automationpractice.com/index.php?controller=my-account"
    email = "bpb@online.com"
    password = "bpb"
    data_file="SeleniumTest/Configurations/Registrationdata.json"
    def __init__(self):
        pass

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



tdata = TestData()
tdata.SeeData()              
