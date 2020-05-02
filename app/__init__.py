from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap
#initializing the application
app = Flask(__name__)

#where we setup the app configurations
app.config.from_object(DevConfig)

#where I initialize flask extensions
bootstrap = Bootstrap(app)

from app import views