__author__ = 'Chris'

import json
from flask import jsonify, Response

from app.database.models.team import Team
from app.database.models.user import Student


def get_team(team_id):
    team = Team.objects(tid=team_id).first()

    if team is not None:
        members = []
        users = team.user_ids
        for x in range(0, len(users)):
            student = Student.objects(uid=users[x]).exclude('encrypt_pw').first()
            if student is not None:
                members.append(json.dumps({'name': student.full_name,
                                           'uid': student.uid
                                           })
                               )

        resp = jsonify(team_id=team.tid,
                       name=team.name,
                       members=members)
        resp.status = '200'

        return resp

    else:
        return Response(status=404)


def put_team(team_id, args):
    team = Team.objects(tid=team_id).first()

    try:
        team
    except AttributeError:
        return Response(status=404)


def delete_team(team_id):
    try:
        team = Team.objects(tid=team_id).first()
        team.delete()

        return Response(status=204)
    except AttributeError:
        return Response(status=400)
