from flask import jsonify, current_app, g, Response
from app.database.models.course import Course

def get_course(course_id):
	course = Course.objects(cid=course_id).first()
	if course is not None:
		return jsonify(course_id=course.cid,
                           name=course.name,
                           description=course.descr,
                           projects=course.proj_ids)
	return jsonify({})
	
def make_course(args):
	course = Course.init_course(args['name'], args['desc'], [], [], args['instructor'])
	return Response(status=201)