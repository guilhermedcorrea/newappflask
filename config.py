import pyodbc
from sqlalchemy import create_engine
import dotenv
import os
from urllib.parse import quote_plus
from sqlalchemy import text


dotenv.load_dotenv(dotenv.find_dotenv())
driver = os.getenv('driver')
Server = os.getenv('server')
usuario = os.getenv('usuario')
tabela = os.getenv('database')
password = os.getenv('password')


def get_connection():
    connection_string = """{};SERVER={};DATABASE={};UID={};PWD={}""".format(driver,Server,tabela,usuario,password)
    url_db = quote_plus(connection_string)
    connection_url = f'mssql+pyodbc:///?odbc_connect=+{url_db}'
    return create_engine(connection_url,fast_executemany=True)