__author__ = 'Chris'

from flask import jsonify, current_app, g, Response
from flask_login import current_user


def get_current_user():
    if current_user.is_authenticated():

        if current_user.type == 'u':
            resp = jsonify(success=True, uid=current_user.uid,
                           first=current_user.first_name, last=current_user.last_name,
                           username=current_user.username, type=current_user.type,
                           courses=current_user.team_ids)

            resp.status = '200'
            return resp

        elif current_user.type == 'i':
            resp = jsonify(success=True, uid=current_user.uid,
                           first=current_user.first_name, last=current_user.last_name,
                           username=current_user.username, type=current_user.type,
                           courses=current_user.class_ids)

            resp.status = '200'
            return resp

    else:
        resp = jsonify(success=False)
        resp.status = '401'
        return resp

def put_user(args=None):
    if current_user.is_authenticated():
        try:
            current_user.first_name = args['first']
            current_user.last_name = args['last']
            current_user.save()
        except Exception:
            pass
        return Response(status=201)
    else:
        resp = jsonify(success=False)
        resp.status = '404'
        return resp