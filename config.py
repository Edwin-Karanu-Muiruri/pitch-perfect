import os
class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    '''
    Production config child class
    '''
    pass

class DevConfig(Config):
    '''
    Develpment config child class
    '''
    DEBUG = True