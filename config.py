import os
import configparser

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    config = configparser.ConfigParser()
    config.read_file(open('azure.cfg'))

    RESOURCE_GROUP              = config.get('RESOURCE','RESOURCE_GROUP')
    LOCATION                    = config.get('RESOURCE','LOCATION')
    SQL_SERVER                  = config.get("SQL","SQL_SERVER")
    SQL_DATABASE                = config.get("SQL","SQL_DATABASE")
    SQL_ADMIN_USER              = config.get("SQL","SQL_ADMIN_USER")
    SQL_ADMIN_PASSWORD          = config.get("SQL","SQL_ADMIN_PASSWORD")
    SQL_SKU                     = config.get("SQL","SQL_SKU")
    SQL_EDITION                 = config.get("SQL","SQL_EDITION")
    STORAGE_ACCOUNT_NAME        = config.get("STORAGE","STORAGE_ACCOUNT_NAME")
    STORAGE_CONTAINER_NAME      = config.get("STORAGE","STORAGE_CONTAINER_NAME")
    STORAGE_BLOB_STORAGE_KEY    = config.get("STORAGE","STORAGE_BLOB_STORAGE_KEY")
    STORAGE_SKU                 = config.get("STORAGE","STORAGE_SKU")
    STORAGE_KIND                = config.get("STORAGE","STORAGE_KIND")
    APP_NAME                    = config.get("APP","APP_NAME")
    APP_SERVICE_PLAN_NAME       = config.get("APP","APP_SERVICE_PLAN_NAME")
    APP_SKU                     = config.get("APP","APP_SKU")
    APP_RUNTIME                 = config.get("APP","APP_RUNTIME")
    AAD_APP_NAME                = config.get("AAD","AAD_APP_NAME")
    REDIRECT_URL                = config.get("AAD","REDIRECT_URL")
    AAD_CLIENT_SECRET           = config.get("AAD","AAD_CLIENT_SECRET")
    AAD_CLIENT_ID               = config.get("AAD","AAD_CLIENT_ID")

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or f'{STORAGE_ACCOUNT_NAME}'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or f'{STORAGE_BLOB_STORAGE_KEY}'
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or f'{STORAGE_CONTAINER_NAME}'

    SQL_SERVER = os.environ.get('SQL_SERVER') or f'{SQL_SERVER}.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or f'{SQL_DATABASE}'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or f'{SQL_ADMIN_USER}'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or f'{SQL_ADMIN_PASSWORD}'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = f"{AAD_CLIENT_SECRET}"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = f"{AAD_CLIENT_ID}"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session