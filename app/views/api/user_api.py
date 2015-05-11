__author__ = 'Chris'

from flask import jsonify, current_app, g, Response
from flask_restful import Resource, reqparse
from flask_login import current_user

from app.database.models.user import User


class UserApi(Resource):

    def get(self):
        if current_user.is_authenticated():
            g.logger.info("Returning User Info: " + current_user.full_name)

            resp = jsonify(success=True, uid=current_user.uid,
                           first=current_user.first_name, last=current_user.last_name,
                           username=current_user.username, type=current_user.type,
                           courses=current_user.team_ids)

            resp.status = '200'
            return resp
        else:
            resp = jsonify(success=False)
            resp.status = '401'
            return resp

    def post(self):
        return Response(status=405)

    def put(self):
        pass

    def delete(self):
        return Response(status=405)