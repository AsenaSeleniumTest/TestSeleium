import os
import google.generativeai as gen
from google import genai 

class ConnectAI:
    
    def __init__(self,key):
        self.genkey = key

    def get_genai_client(self):
        return genai.Client(api_key=self.genkey)

    def get_response(self):
        client= self.get_genai_client()
        response = client.models.generate_content(model="gemini-2.0-flash",contents="Give me sample test in python using behave")
        return response    

gen.configure(api_key=os.environ['API_KEY'])



