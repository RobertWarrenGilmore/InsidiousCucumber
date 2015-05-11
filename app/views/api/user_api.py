__author__ = 'Chris'

from flask import jsonify, current_app, g
from flask_restful import Resource, reqparse
from flask_login import current_user

from app.database.models.user import User


class UserApi(Resource):

    def get(self):
        if current_user.is_authenticated():
            g.logger.info("Returning User Info: " + current_user.full_name)

            return jsonify(message="Returned User Object")
        else:
            return jsonify(message="User not Authenticated")

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass