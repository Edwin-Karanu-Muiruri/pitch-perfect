import os
class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://edwin:EDUcaranow98@localhost/pitchperfect'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

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

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}