import os 

class Config(object):
    DEBUG = True
    DATABASE_FILE = os.path.join('database', 'DB_wish.db')
    SECRET_KEY = os.urandom(12)
