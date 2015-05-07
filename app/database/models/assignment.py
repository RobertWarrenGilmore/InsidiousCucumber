""" Created on Apr 6, 2015

@author: chris, Randy
"""

from mongoengine.document import Document
from mongoengine.fields import IntField, DateTimeField, StringField


class Assignment(object):

    # Set the collection name used in the database
    config_collection_name = "assignments"

    aid = IntField()
    class_id = IntField()
    due = DateTimeField()
    description = StringField()

    def __init__(self, aid, class_id, due, description):
        self.aid = aid
        self.class_id = class_id
        self.due = due
        self.description = description


class Deliverable(Document, Assignment):
    assigned_team = IntField()

    def __init__(self, aid, class_id, due, description, team=None):
        super(self.__class__, self).__init__(aid, class_id, due, description)
        self.assigned_team = team


class Task(Document, Assignment):
    assigned_user = IntField()

    def __init__(self, aid, class_id, due, description, user=None):
        super(self.__class__, self).__init__(aid, class_id, due, description)
        self.assigned_user = user