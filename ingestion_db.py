# Use this script to save csv files into database with their filename as tablename
import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

logging.basicConfig(
    filename="ingestion_db.py", 
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s", 
    filemode="a"  
)

engine = create_engine('sqlite:///inventory.db')

def ingest_db(df, table_name, engine):
    '''this function will ingest the dataframe into database table'''
    df.to_sql(table_name, con = engine, if_exists = 'replace', index = False)
    
def load_raw_data():
    '''this function will load the CSVs as dataframe and ingest into db'''
    start = time.time()
    for file in os.listdir('data'):
        if '.csv' in file:
            df = pd.read_csv('data/'+file)
            logging.info(f'Ingesting {file} in db')
            ingest_db(df, file[:-4], engine)
    end = time.time()
    total_time = (end - start)/60
    logging.info('--------------Ingestion Complete------------')
    
    logging.info(f'\nTotal Time Taken: {total_time} minutes')

if __name__ == '__main__':
    load_raw_data()

2025-12-06 15:23:28,521 - INFO - Ingesting begin_inventory.csv in db
2025-12-06 15:23:34,992 - INFO - Ingesting end_inventory.csv in db
2025-12-06 15:23:46,826 - INFO - Ingesting purchases.csv in db
2025-12-06 15:25:21,271 - INFO - Ingesting purchase_prices.csv in db
2025-12-06 15:25:52,410 - INFO - Ingesting sales.csv in db
