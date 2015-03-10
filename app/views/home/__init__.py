from flask import Blueprint, render_template, make_response, jsonify


mod = Blueprint('home', __name__)

@mod.route('/')
def index():
    return make_response(open('app/static/base.html').read())

@mod.route('/angularUpdate', methods=['GET'])
def popAngular():
    return jsonify(mode="Development")
