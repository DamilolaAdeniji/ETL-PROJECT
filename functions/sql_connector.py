import pymssql
import pandas as pd
import os

from dotenv import load_dotenv
load_dotenv()

USERNAME = str(os.environ['USERNAME'])
PASSWORD = str(os.environ['PASSWORD'])
DATABASE = str(os.environ['DATABASE'])
SERVER = str(os.environ['SERVER'])


def read_sql(query):
    conn = pymssql.connect(server=SERVER,user=USERNAME, password=PASSWORD, database=DATABASE,conn_properties='')
    cursor = conn.cursor(as_dict=True)
    cursor.execute(query)
    data=cursor.fetchall()
    return pd.DataFrame(data)

def write_sql(query):
    conn = pymssql.connect(server=SERVER,user=USERNAME, password=PASSWORD, database=DATABASE,conn_properties='')
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()

