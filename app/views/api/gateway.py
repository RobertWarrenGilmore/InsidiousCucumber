'''
Created on Apr 6, 2015

@author: chris
'''

from flask import jsonify, current_app
from flask_restful import Resource, reqparse

from app.database.User import Student, Instructor

logger = current_app.config['APP_LOGGER']
print(logger)

class Login(Resource):
    def get(self):
        return get_login_info()
    
def get_login_info():
    
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str)
    parser.add_argument('password', type=str)
    args = parser.parse_args()
    
    logger.info("This is a test log")
    
    stu = Student.get_student_by_name(args['name'])
    if stu is not None:
        if stu.check_password(args['password']):
            retDic = {}
            retDic['user'] = stu.__dict__
            retDic['professor'] = False
            return jsonify(retDic)
    return jsonify({'logggedin':False})
    
    instruct = Instructor.get_instructor_by_name(args['name'])
    if instruct is not None:
        if stu.check_password(args['password']):
            retDic = {}
            retDic['user'] = instruct
            retDic['professor'] = False
            return jsonify(retDic)
    return jsonify({'logggedin':False})