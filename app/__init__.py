from flask import Flask, g
from flask_restful import Api
from flask_login import LoginManager
from flask_mongoengine import MongoEngine

# create the app
minerva = Flask(__name__)

# Configure the app using a class found in settings.py
minerva.config.from_object('app.settings.DevConfig')

# add the API
api = Api(minerva)

# add login manager
login = LoginManager(minerva)
login.session_protection = "strong"

# add the database connection
db = MongoEngine(minerva)

# configure the logger
logger = minerva.config['APP_LOGGER']
logger.info("Logger created")

# Push the current application context to allow for current_app to be used
app_ctx = minerva.app_context()
app_ctx.push()

# Register all of the blueprints
from views import home, auth
minerva.register_blueprint(home.mod)
minerva.register_blueprint(auth.mod, url_prefix='/auth')

# Register the REST apis
from app.views.api import UserApi, CourseApi, TeamApi, ProjectApi
api.add_resource(UserApi, '/user')
api.add_resource(CourseApi, '/course/<int:course_id>')
api.add_resource(TeamApi, '/team/<int:team_id>')
api.add_resource(ProjectApi, '/project/<int:project_id>')

@minerva.before_request
def config_g():
    g.logger = logger

@minerva.teardown_request
def clean_g(exception=None):
    g.logger = None
