import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\xd6\x04\xbdj\xfe\xed$c\x1e@\xad\x0f\x13,@G'
    MONGODB_SETTINGS = {
        'host':'mongodb+srv://ipvidanova:RN799n93Pb!n@cluster0-rz95e.azure.mongodb.net/lista-presenca?retryWrites=true&w=majority'
    }