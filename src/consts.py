from os import getenv, path
from dotenv import load_dotenv
 
load_dotenv(path.dirname(__file__) + '/../.env')
 
# Application
 
APP_HOST = getenv('APP_HOST')
APP_PORT = getenv('8000')
 
# Storage
 
STORAGE_PATH = getenv('STORAGE_PATH')
 
# Database
 
DB_HOST = getenv('DB_HOST')
DB_PORT = getenv('DB_PORT')
DB_USER = getenv('DB_USER')
DB_PASS = getenv('DB_PASS')
DB_NAME = getenv('DB_NAME')
 
DB_CONNECTION_STRING = f'mssql+pyodbc://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'