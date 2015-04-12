import pymongo

from flask import current_app

#DB Setup
__client = pymongo.MongoClient(current_app.config['DB_CONNECTION'])
db = __client[current_app.config['DB_NAME']]