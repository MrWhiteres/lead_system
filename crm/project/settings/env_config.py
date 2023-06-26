from os import environ

from dotenv import load_dotenv

load_dotenv()

DJANGO_KEY = environ.get('KEY')
DJANGO_DEBUG = environ.get('DEBUG')
DB_NAME = environ.get('DB_NAME')
DB_USER = environ.get('DB_USER')
DB_PASSWORD = environ.get('DB_PASSWORD')
DB_HOST = environ.get('DB_HOST')
