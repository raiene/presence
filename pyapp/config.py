import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'nao-te-interessa'
    MONGODB_SETTINGS = {
        'host': os.environ.get('MONGO_HOST') or 'mongol'
    }