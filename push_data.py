import os
import sys
import json

from dotenv import load_dotenv
load_dotenv() #initlize 

MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL) #python push_data.py to test if env connected?


import certifi #to make secure/trusted/valid html connection .in this case it is mongodb
ca=certifi.where() #gives bundel of ca certificates

import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract(): #responsible for etl pipeline
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_to_json_convertor(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True) #remove the index on left 
            records=list(json.loads(data.T.to_json()).values()) #T is transpose(r becomes c and vica versa)
            '''
            after transpose:-
    {"0": {"col1": "value1", "col2": "value2"},
    "1": {"col1": "value3", "col2": "value4"}}
    json.loads convets the json to python dict
    .values gives the values of the dict i.e the records/rows
    list converts the values to list
    therefore records= json [
    {'col1': 'value1', 'col2': 'value2'},
    {'col1': 'value3', 'col2': 'value4'},
    ...
]
            '''
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records

            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]
            
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return(len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
if __name__=='__main__':
    FILE_PATH="Network_Data\phisingData.csv"
    DATABASE="PALAK"
    Collection="NetworkData" # table name
    networkobj=NetworkDataExtract()
    records=networkobj.csv_to_json_convertor(file_path=FILE_PATH)
    print(records)
    no_of_records=networkobj.insert_data_mongodb(records,DATABASE,Collection)
    print(no_of_records)
        


