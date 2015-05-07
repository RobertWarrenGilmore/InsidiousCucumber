""" Created on Apr 6, 2015

@author: chris, Randy
"""

from mongoengine.document import Document
from mongoengine.fields import StringField, IntField, ListField


class Team(Document):

    config_collection_name = 'teams'

    tid = IntField()
    name = StringField()
    user_ids = ListField(IntField())
    message_ids = ListField(IntField())
    assign_ids = ListField(IntField())
    meeting_ids = ListField(IntField())

    def __init__(self, tid, name, user_ids, message_ids=[], assign_ids=[], meeting_ids=[]):
        self.tid = tid
        self.name = name
        self.user_ids = user_ids
        self.message_ids = message_ids
        self.assign_ids = assign_ids
        self.meeting_ids = meeting_ids