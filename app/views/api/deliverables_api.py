__author__ = 'chris'

from flask import jsonify

from app.database.models.assignment import Deliverable
from app.database.models.project import Project

def get_deliverables(args):
    project = Project.objects(pid=args['project_id']).first()

    deliv_data = []

    for i, deliv in enumerate(project.deliverable_ids):
        deliverable = Deliverable.objects(aid=deliv).first()
        deliv_data.append(jsonify({'title': deliverable.description, 'start': deliverable.start}))
