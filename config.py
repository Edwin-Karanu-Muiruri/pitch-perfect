import os
class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = 'EdwinKaranu'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    '''
    Production config child class
    '''
    pass

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://edwin:EDUcaranow98@localhost/pitchperfect_test'


class DevConfig(Config):
    '''
    Develpment config child class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://edwin:EDUcaranow98@localhost/pitchperfect'
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}


