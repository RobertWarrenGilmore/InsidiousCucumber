"""Application Gateway

@author: chris
"""

from flask import jsonify, current_app, Response
from flask_restful import Resource, reqparse

from app.database.models import Course, Project, Team, Student
from user_api import get_current_user, put_user
from team_api import get_team, delete_team
from project_api import get_project, make_project, update_project, delete_project
from course_api import get_course, make_course


class UserApi(Resource):
    def get(self):
        return get_current_user()

    def post(self):
        return Response(status=405)

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('first', type=str)
        parser.add_argument('last', type=str)
        args = parser.parse_args()
        return put_user(args)

    def delete(self):
        return Response(status=405)


class TeamApi(Resource):
    def get(self, team_id):
        return get_team(team_id)

        team = Team.objects(tid=team_id).first()

        if team is not None:
            member_names = []
            users = team.user_ids
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
        return Response(status=405)

    def put(self, team_id):
        pass

    def delete(self, team_id):
        return delete_team(team_id)


class CourseApi(Resource):
    def get(self, course_id):
        course = Course.objects(cid=course_id).first()
        if course is not None:
            return jsonify(course_id=course.cid, name=course.name, description=course.descr, projects=course.proj_ids)
        return jsonify({})

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass


class CreateCourseApi(Resource):
    def get(self):
        return Response(status=405)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('desc', type=str)
        parser.add_argument('instructor', type=int)
        args = parser.parse_args()

        return make_course(args)

    def put(self):
        return Response(status=405)

    def delete(self):
        return Response(status=405)


def delete(self):
    pass


class CreateProjApi(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('url', type=str)
        parser.add_argument('desc', type=str)
        args = parser.parse_args()

        return make_project(args)

    def get(self, project_id):
        pass

    def put(self):
        pass

    def delete(self):
        pass


class ProjectApi(Resource):
    def get(self, project_id):
        return get_project(project_id)

    def post(self):
        return Response(status=405)

    def put(self, project_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('url', type=str)
        parser.add_argument('description', type=str)
        parser.add_argument('team_ids', type=list)
        parser.add_argument('deliverable_ids', type=list)
        args = parser.parse_args()

        return update_project(project_id, args)

    def delete(self, project_id):
        return delete_project(project_id)


class MessageApi(Resource):
    def get(self, message_id):
        pass

    def post(self, message_id):
        return Response(status=405)

    def put(self, message_id):
        return Response(status=405)

    def delete(self, message_id):
        pass