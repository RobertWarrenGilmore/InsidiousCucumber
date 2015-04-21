'''
Created on Apr 20, 2015

@author: chris
'''

from flask import Blueprint, request, redirect, url_for, jsonify
from flask_login import login_user, logout_user, login_required

from app.database.models.user import Student, Instructor


mod = Blueprint('auth', __name__)

@mod.route('/login', methods=['POST'])
def login():
    
    stuMap = Student.get({'username': request.args['username']})
    if stuMap is not None:
        student = Student.parse_doc(stuMap)
        if student.check_password(request.args['password']):
            login_user(student)
            student.type = 'u'
            resp = jsonify(student)
            resp['success'] = True
            return resp
    
    instructMap = Instructor.get({'username': request.args['username']})
    if instructMap is not None:
        instructor = Instructor.parse_doc(instructMap)
        if instructor.check_password(request.args['password']):
            login_user(instructor)
            instructor.type = 'u'
            resp = jsonify(instructor)
            resp['success'] = True
            return resp
        
    return jsonify({'success':False})


@mod.route('/logout')
@login_required
def logout():
    """Log the user out and update user.last_seen."""
    logout_user()
    
    return redirect(url_for('home.home'))
