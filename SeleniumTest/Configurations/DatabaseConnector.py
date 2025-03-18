import mysql.connector
import os
import SQLServerConnector 

class DataBaseConnector:
    def __init__(self):
        self.host = "localhost"


    def connect_to_database(self,query):
        try:
            connection = mysql.connector.connect(
                host=self.host,query=query )
            return connection
        except mysql.connector.Error as ex:
            print(f"Error connecting to database: {ex.__str__()}")

    def execute_query(self,connection,query):
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            return cursor 
        except mysql.connector.Error as ex:
            print(f"Error executing query: {ex.__str__()}")
            return ex

    