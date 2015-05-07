""" Created on Apr 6, 2015

@author: chris
"""

from mongoengine.document import Document
from mongoengine.fields import StringField, IntField, ListField, SequenceField


class Team(Document):

    meta = {'collection': 'teams'}

    tid = SequenceField(required=True, unique=True, primary_key=True)
    name = StringField(required=True)
    user_ids = ListField(IntField(), default=[])
    message_ids = ListField(IntField(), default=[])
    assign_ids = ListField(IntField(), default=[])
    meeting_ids = ListField(IntField(), default=[])

    def __init__(self, *args, **kwargs):
        Document.__init__(*args, **kwargs)

        if 'tid' in kwargs:
            self.tid = kwargs['tid']
        if 'name' in kwargs:
            self.name = kwargs['name']
        if 'user_ids' in kwargs:
            self.user_ids = kwargs['user_ids']
        if 'message_ids' in kwargs:
            self.message_ids = kwargs['message_ids']
        if 'assign_ids' in kwargs:
            self.assign_ids = kwargs['assign_ids']
        if 'meeting_ids' in kwargs:
            self.meeting_ids = kwargs['meeting_ids']

    @staticmethod
    def init_team(name):
        tid = Team.objects.count() + 1
        return Team(tid=tid, name=name)