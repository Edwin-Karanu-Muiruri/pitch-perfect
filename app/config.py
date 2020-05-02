class Config:
    '''
    General configuration parent class
    '''
    pass

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