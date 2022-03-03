#import db
import psycopg2
from sqlalchemy import create_engine
from .transform import BaseTransformer


class Db:
    def load_to_db(self,table_name, engine, dataframe):
        engine=create_engine(engine)
        #engine = create_engine('postgresql://username:password@localhost:5432/mydatabase')
        dataframe.to_sql(table_name, engine, if_exists='replace',
                index=False)




    #from sqlalchemy import create_engine

    #df.to_sql('table_name', engine)





    def read_from_db(self,sql_query, conn_string):
        #conn_string=ConfigReader()
        #conn_string=conn_string.configuration() 
        conn = psycopg2.connect(conn_string)

        #Setting auto commit false
        conn.autocommit = True

        #Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        #Retrieving data
        cursor.execute(sql_query)

        #Fetching 1st row from the table
        result = cursor.fetchone();
        print(result)

        #Fetching 1st row from the table
        result = cursor.fetchall();
        print(result)

        #Commit your changes in the database
        conn.commit()

        #Closing the connection
        conn.close()
