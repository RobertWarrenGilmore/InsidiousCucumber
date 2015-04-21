'''
Created on Apr 6, 2015

@author: chris
'''

from flask import jsonify, current_app
from flask_restful import Resource
from flask_login import current_user


logger = current_app.config['APP_LOGGER']

class UserApi(Resource):
    def get(self):
        if current_user.is_authenticated():
            userDict = {'first': current_user.first,
                        'last': current_user.last,
                        'username': current_user.username,
                        }
            logger.info("Returning User Info: " + str(userDict))
            
            return jsonify(userDict)

class TeamApi(Resource):
    pass

class CourseApi(Resource):
    pass

class ProjectApi(Resource):
    pass

class TeamPrefApi(Resource):
    pass