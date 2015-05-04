"""Created on Apr 6, 2015

@author: chris, Randy
"""

from mongoalchemy.document import Document
from mongoalchemy.fields import StringField, IntField
from app.database.models.common import CommonEqualityMixin
from mongoalchemy.fields.fields import BoolField


class BasicMessage(CommonEqualityMixin, object):

    config_collection_name = "messages"

    mid = IntField()
    text = StringField()
    sender = IntField()
    seen = BoolField()
    type = StringField()
    
    def __init__(self, mid, text, sender):
        self.mid = mid
        self.text = text
        self.sender = sender
        
    def mark_as_seen(self):
        self.seen = True


class UserMessage(Document, BasicMessage):

    receiver = IntField()
    
    def __init__(self, mid, text, sender, receiver):
        super(self.__class__, self).__init__(mid, text, sender)
        self.receiver = receiver
        self.type = "user"
        self.seen = False


class TeamMessage(Document, BasicMessage):

    team = IntField()
    
    def __init__(self, mid, text, sender, team):
        super(self.__class__, self).__init__(mid, text, sender)
        self.team = team
        self.type = "team"