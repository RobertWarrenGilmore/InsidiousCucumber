from flask import Flask, g


#create the app
minerva = Flask(__name__)

#Configure the app using a class found in settings.py
minerva.config.from_object('app.settings.DevConfig')

logger = minerva.config['LOGGER']
logger.info("Logger created")

#Register all of the blueprints

from views import home
from app.views import api
minerva.register_blueprint(home.mod)
minerva.register_blueprint(api.mod, url_prefix='/metar')

@minerva.before_request
def config_g():
    g.logger = logger

@minerva.teardown_request
def clean_g(exception=None):
    g.logger = None
