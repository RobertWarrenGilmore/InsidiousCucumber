"""Application Gateway

@author: chris
"""

from flask import jsonify, current_app
from flask_restful import Resource, reqparse

from app.database.models import Course, Project, Team, Student
from user_api import UserApi

logger = current_app.config['APP_LOGGER']


class TeamApi(Resource):

    def get(self, team_id):

        team = Team.objects(tid=team_id).first()

        if team is not None:
            member_names = []
            users = team.user_ids
            logger.info(str(users))
            for x in range(0, len(users)):
                student = Student.objects(uid=users[x]).exclude('encrypt_pw').first()
                if student is not None:
                    member_names.append(student.full_name)

            return jsonify(team_id=team.tid,
                           name=team.name,
                           members=member_names
                           )
        return jsonify(message="Team Not Found")

    def post(self, team_id):
        pass

    def put(self, team_id):
        pass

    def delete(self, team_id):
        pass


class CourseApi(Resource):
    def get(self, course_id):

        course = Course.objects(cid=course_id).first()
        if course is not None:
            return jsonify(course_id=course.cid,
                           name=course.name,
                           description=course.descr,
                           projects=course.proj_ids)
        return jsonify({})

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass


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

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass


class TeamPrefApi(Resource):
    pass