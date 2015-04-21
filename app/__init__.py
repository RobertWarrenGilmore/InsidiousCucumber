from flask import Flask, g
from flask_restful import Api
from flask_login import LoginManager

#create the app
minerva = Flask(__name__)

#add the API
api = Api(minerva)
login = LoginManager(minerva)

login.session_protection = "strong"

#Configure the app using a class found in settings.py
minerva.config.from_object('app.settings.DevConfig')

logger = minerva.config['APP_LOGGER']
logger.info("Logger created")

# Push the current application context to allow for current_app to be used
app_ctx = minerva.app_context()
app_ctx.push()
    
#Register all of the blueprints
from views import home, auth
minerva.register_blueprint(home.mod)
minerva.register_blueprint(auth.mod, url_prefix='/auth')

from app.views.api.gateway import UserApi, CourseApi, TeamApi, ProjectApi 
api.add_resource(UserApi, '/user')
api.add_resource(CourseApi, '/course')
api.add_resource(TeamApi, '/team')
api.add_resource(ProjectApi, '/project')

@minerva.before_request
def config_g():
    g.logger = logger

@minerva.teardown_request
def clean_g(exception=None):
    g.logger = None
