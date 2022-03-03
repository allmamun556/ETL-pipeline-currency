from etl.transform import BaseTransformer
from etl.load import Db



def main():
    ''' import the file '''
    import_file=BaseTransformer().db_load() #Instatiate a  object from ImportFile class
    #data=import_file.db_load()
    print(import_file)

    '''Transform the dataset based on your requirements'''
    convert_currency=BaseTransformer().convert_us_to_gbp(import_file,['BTC','ETH','XRP','LTC']) #Instatiate a object from this class

    #transform_column=BaseTransformer.required_column(convert_currency)

    transform_col=BaseTransformer().required_column(convert_currency)

    print(transform_col)

    #BaseTransformer().connect_engine()

    Db().load_to_db('currency', BaseTransformer().configuration(),transform_col)
    data=Db().read_from_db('''SELECT * from currency''',BaseTransformer().configuration()) 
    #return data
    #print(data)
    return data


main()
 