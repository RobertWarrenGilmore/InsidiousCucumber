from flask import Blueprint, render_template, make_response, jsonify

mod = Blueprint('home', __name__)


@mod.route('/')
def index():
    """ Start the Angular App """
    return make_response(open('app/static/base.html').read())