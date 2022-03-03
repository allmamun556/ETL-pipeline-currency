
import pandas as pd
from sqlalchemy import create_engine
import configparser 
from configparser import ConfigParser
import psycopg2


class ImportFile:
    def __init__(self):
        self.mamun='mamun'
        #self.__sharif='sharif'
    def db_load(self):
        crypto_df = pd.read_csv('data/crypto-markets.csv')
        crypto_df.head()
        return crypto_df

#data=ImportFile()
#data=data.db_load()
#print(data)
#above class is working fine


class ConfigReader(ImportFile):  #Inheretencing attribute from parent class
 def __init__(self):
     super().__init__()
 def configuration(self):
    configur=ConfigParser()
    configur.read("C:\\Users\\z5iksxt\\project\\ETL pipeline\etl\\configfile.ini")
    user=configur.get('DB','user')
    host=configur.get('DB','host')
    password=configur.get('DB','password')
    dbname=configur.get('DataBase','dbname')
    conn_string = "postgresql://{}:{}@{}/{}".format(user, password, host, dbname)
    return conn_string

 def connect_engine(self,conn_string):    
    db_sql = create_engine(conn_string)
    conn = db_sql.connect()
    return conn


#print(ConfigReader().mamun) #accesing public variables 
#print(ConfigReader().__sharif) # This is privet variable . so access is not possible
