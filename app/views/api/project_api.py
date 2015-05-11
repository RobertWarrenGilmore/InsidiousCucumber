from flask import jsonify, current_app, g, Response
from app.database.models.project import Project

def get_project(id):
	project = Project.objects(pid=id).first()
	if project is not None:
		return jsonify(project_id=project.pid,
					name=project.name,
					description=project.descr,
					url=project.url,
					team_ids=project.team_ids,
					deliverables = project.deliverable_ids
					)
	return jsonify({})