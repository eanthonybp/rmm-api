import os

SECRET_KEY = 'ReallyReallySecret'
DEBUG = True
DB_USERNAME = "esanthony"
DB_PASSWORD = ""
RMMAPI_DATABASE_NAME = "rmmapi"
DB_HOST = os.getenv('IP','0.0.0.0')
DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME,DB_PASSWORD,DB_HOST,RMMAPI_DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True