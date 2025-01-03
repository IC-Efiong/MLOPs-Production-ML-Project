import sys
from us_visa.exception import USvisaException
from us_visa.logger import logging
import os
from us_visa.costants import DATABASE_NAME, MONGODB_URL_KEY
import pymongo
import certifi

ca = certifi.where()

class MongoDBCLient:
    """
    Class Name :   export_data_into_feature_store
    Description :   This method exports the dataframe from mongodb feature store as dataframe 
    
    Output      :   connection to mongodb database
    On Failure  :   raises an exception
    """
    client = None
    
    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBCLient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise Exception(f"Environment key: {MONGODB_URL_KEY} is not set.")
                MongoDBCLient.client = pymongo.MongoClient(mongo_db_url, tlsCAfile=ca)
            self.client = MongoDBCLient.client
            self.database = self.client[database_name]
            self.databse_name = database_name
            logging.info("MongoDB connection successful")
        except Exception as e:
            raise USvisaException(e,sys)        