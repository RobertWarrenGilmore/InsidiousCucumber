'''
Created on Apr 6, 2015

@author: chris
'''

from flask import jsonify, current_app
from flask_restful import Resource, reqparse
from flask_login import current_user

from app.database.models import Course, Project, Team, Student

logger = current_app.config['APP_LOGGER']

class UserApi(Resource):
    def get(self):
        if current_user.is_authenticated():
            logger.info("Returning User Info: " + current_user.first_name + " " + current_user.last_name)

            
            return jsonify(first=current_user.first_name,
                           last=current_user.last_name,
                           username=current_user.username,
                           type=current_user.type
                           )
        else:
            return jsonify({})

class TeamApi(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('team_id', type=int)
        args = parser.parse_args()
        
        logger.info(args)
        
        teamMap = Team.get({'tid': args['team_id']})
        if teamMap is not None:
            member_names = []
            users = teamMap['user_ids']
            logger.info(str(users))
            for x in range(0, len(users)):
                user_id = users[x]
                stuMap = Student.get({'uid': user_id})
                logger.info(stuMap)
                if stuMap is not None:
                    full_name = stuMap['first_name'] + ' ' + stuMap['last_name']
                    member_names.append(full_name)
            return jsonify(team_id=teamMap['tid'],
                           name=teamMap['name'],
                           members=member_names
                           )
        return jsonify({})

class CourseApi(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('course_id', type=int)
        args = parser.parse_args()
        
        courseMap = Course.get({'cid': args['course_id']})
        if courseMap is not None:
            return jsonify(course_id=courseMap['cid'],
                           name=courseMap['name'],
                           description=courseMap['descr'],
                           projects=courseMap['proj_ids'])
        return jsonify({})

class ProjectApi(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('project_id', type=int)
        args = parser.parse_args()
        
        projMap = Project.get({'pid':args['project_id']})
        if projMap is not None:
            return jsonify(project_id=projMap['pid'],
                           name=projMap['name'],
                           description=projMap['descr'],
                           url=projMap['url'],
                           num_teams=len(projMap['teams'])
                           )
        return jsonify({})
        
class TeamPrefApi(Resource):
    pass