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
	
def make_project(args):
	project = Project.init_project(args['name'],args['url'],args['desc'])
	project.save()
	return Response(status=201)
	
def update_project(id,args):
	project = Project.objects(pid=id).first()
	if project is not None:
		project.name = args['name']
		project.url = args['url']
		project.descr = args['description']
		project.team_ids = args['team_ids']
		project.deliverable_ids = args['deliverable_ids']
		project.save()
		return Response(status=201)
	return Response(status=404)