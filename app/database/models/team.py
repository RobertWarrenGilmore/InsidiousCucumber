"""
Created on Apr 6, 2015

@author: chris, Randy
"""

from mongoalchemy.document import Document
from mongoalchemy.fields import StringField, IntField, ListField


class Team(Document):

    config_collection_name = 'teams'

    tid = IntField()
    name = StringField()
    user_ids = ListField()
    message_ids = ListField()
    assign_ids = ListField()
    meeting_ids = ListField()

    def __init__(self, tid, name, user_ids, message_ids=[], assign_ids=[], meeting_ids=[]):
        self.tid = tid
        self.name = name
        self.user_ids = user_ids
        self.message_ids = message_ids
        self.assign_ids = assign_ids
        self.meeting_ids = meeting_ids
        
    def add_message(self, tid):
        pass
        
    def add_assignment(self, tid):
        pass
        
    def add_meeting(self, tid):
        pass