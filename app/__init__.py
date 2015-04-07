from flask import Flask, g
from flask_restful import Api

#create the app
minerva = Flask(__name__)

#add the API
api = Api(minerva)

#Configure the app using a class found in settings.py
minerva.config.from_object('app.settings.DevConfig')

logger = minerva.config['APP_LOGGER']
logger.info("Logger created")

# Push the current application context to allow for current_app to be used
app_ctx = minerva.app_context()
app_ctx.push()
    
#Register all of the blueprints
from views import home
minerva.register_blueprint(home.mod)

from app.views.api.gateway import Login
api.add_resource(Login, '/login')

@minerva.before_request
def config_g():
    g.logger = logger

@minerva.teardown_request
def clean_g(exception=None):
    g.logger = None
