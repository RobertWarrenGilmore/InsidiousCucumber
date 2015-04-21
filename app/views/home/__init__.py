from flask import Blueprint, render_template, make_response, jsonify


mod = Blueprint('home', __name__)

""" Start the Angular App """
@mod.route('/')
def index():
    return make_response(open('app/static/base.html').read())