'''
Created on Apr 20, 2015

@author: chris
'''

from flask import Blueprint, request, redirect, url_for, jsonify, json
from flask_login import login_user, logout_user, login_required

from app.database.models.user import Student, Instructor


mod = Blueprint('auth', __name__)

@mod.route('/login', methods=['POST'])
def login():
    data = json.loads(request.data)
    stuMap = Student.get({'username': data["username"]})
    print(stuMap)
    if stuMap is not None:
        student = Student.parse_doc(stuMap)
        if student.check_password(data['password']):
            print(student.to_hashmap())
            login_user(student)
            return jsonify(success=True)
    
    instructMap = Instructor.get({'username': data['username']})
    if instructMap is not None:
        instructor = Instructor.parse_doc(instructMap)
        if instructor.check_password(data['password']):
            login_user(instructor)
            return jsonify(success=True)
        
    return jsonify({'success':False})


@mod.route('/logout')
@login_required
def logout():
    """Log the user out and update user.last_seen."""
    logout_user()
    
    return redirect(url_for('home.home'))
