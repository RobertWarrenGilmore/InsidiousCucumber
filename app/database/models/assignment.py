""" Created on Apr 6, 2015

@author: chris
"""

from mongoengine.document import Document
from mongoengine.fields import IntField, DateTimeField, StringField, SequenceField


class Assignment(Document):

    # Set the collection name used in the database
    meta = {'allow_inheritance': True,
            'collection': 'assignments'}

    aid = SequenceField(required=True, primary_key=True, unique=True)
    class_id = IntField(required=True)
    due = DateTimeField(required=True)
    description = StringField()

    def __init__(self, *args, **kwargs):
        Document.__init__(self, *args, **kwargs)

        if 'aid' in kwargs:
            self.aid = kwargs['aid']
        if 'class_id' in kwargs:
            self.class_id = kwargs['class_id']
        if 'due' in kwargs:
            self.due = kwargs['due']
        if 'description' in kwargs:
            self.description = kwargs['description']


class Deliverable(Assignment):
    assigned_team = IntField(default=None)

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)

        if 'assigned_team' in kwargs:
            self.assigned_team = kwargs['assigned_team']

    @staticmethod
    def init_deliverable(class_id, due, description, assigned_team):
        aid = Assignment.objects.count() + 1
        return Deliverable(aid=aid, class_id=class_id, due=due, description=description, assigned_team=assigned_team)


class Task(Assignment):
    assigned_user = IntField(default=None)

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)

        if 'assigned_user' in kwargs:
            self.assigned_user = kwargs['assigned_user']

    @staticmethod
    def init_task(class_id, due, description, assigned_user):
        aid = Assignment.objects.count() + 1
        return Task(aid=aid, class_id=class_id, due=due, description=description, assigned_team=assigned_user)