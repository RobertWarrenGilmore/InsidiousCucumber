""" Created on Apr 6, 2015

@author: chris
"""

from flask import jsonify, current_app
from flask_restful import Resource, reqparse
from flask_login import current_user

from app.database.models import Course, Project, Team, Student


logger = current_app.config['APP_LOGGER']


class UserApi(Resource):

    def get(self):
        if current_user.is_authenticated():
            logger.info("Returning User Info: " + current_user.full_name)

            return jsonify(first=current_user.first_name,
                           last=current_user.last_name,
                           username=current_user.username,
                           type=current_user.type
                           )
        else:
            return jsonify(message="User not Logged in")

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass


class TeamApi(Resource):

    def get(self, team_id):

        team = Team.objects(tid=team_id).first()

        if team is not None:
            member_names = []
            users = team.user_ids
            logger.info(str(users))
            for x in range(0, len(users)):
                student = Student.objects(uid=users[x]).first()
                if student is not None:
                    member_names.append(student.full_name)

            return jsonify(team_id=team.tid,
                           name=team.name,
                           members=member_names
                           )
        return jsonify(message="Team Not Found")


class CourseApi(Resource):
    def get(self, course_id):
        
        course = Course.objects(cid=course_id).first()
        if course is not None:
            return jsonify(course_id=course.cid,
                           name=course.name,
                           description=course.descr,
                           projects=course.proj_ids)
        return jsonify({})


class ProjectApi(Resource):
    def get(self, project_id):
        
        project = Project.objects(pid=project_id)
        if project is not None:
            return jsonify(project_id=project.pid,
                           name=project.name,
                           description=project.descr,
                           url=project.url,
                           num_teams=len(project.teams)
                           )
        return jsonify({})


class TeamPrefApi(Resource):
    pass