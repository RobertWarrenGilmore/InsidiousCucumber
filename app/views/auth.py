""" Created on Apr 20, 2015

@author: chris
"""

from flask import Blueprint, request, redirect, url_for, jsonify, json
from flask_login import login_user, logout_user, login_required
from mongoalchemy.session import Session

from app.database.models.user import Student, Instructor
from app.database import db

mod = Blueprint('auth', __name__)


@mod.route('/login', methods=['POST'])
def login():
    data = json.loads(request.data)

    try:
        session = Session(db)
        student = session.query(Student).filter_by(Student.username == data["username"] and Student.utype == 'u')

        if student is not None and student.check_password(data['password']):
            login_user(student)
            return jsonify(success=True)

        instructor = session.query(Instructor)\
                            .query(Instructor.username == data["username"] and
                                   Instructor.utype == 'i'
                                   )

        if instructor is not None and instructor.check_password(data['password']):
            login_user(student)
            return jsonify(success=True)

    except Exception:
        return jsonify(message="An Exception was Thrown!")

    finally:
        # session.end()
        pass

    return jsonify({'success': False})


@mod.route('/logout')
@login_required
def logout():
    """Log the user out"""
    logout_user()
    
    return redirect(url_for('home.index'))
