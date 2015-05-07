""" Created on Apr 20, 2015

@author: chris
"""

from flask import Blueprint, request, redirect, url_for, jsonify, json
from flask_login import login_user, logout_user, login_required

from app.database.models.user import User

mod = Blueprint('auth', __name__)


@mod.route('/login', methods=['POST'])
def login():
    data = json.loads(request.data)
    user = User.objects(username=data['username']).first()

    if user is not None and user.verify_password(data['password']):
        login_user(user)
        return jsonify(success=True)

    return jsonify({'success': False})


@mod.route('/logout')
@login_required
def logout():
    """Log the user out"""
    logout_user()
    
    return redirect(url_for('home.index'))
