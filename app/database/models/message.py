'''
Created on Apr 6, 2015

@author: chris, Randy
'''

from app.database.models.common import CommonEqualityMixin
from app.database.mappers.messageMapper import UserMessageMapper, TeamMessageMapper


class BasicMessage(CommonEqualityMixin,object):
    
    def __init__(self, mid, text, sender):
        self.mid = mid
        self.text = text
        self.sender = sender
        
    def mark_as_seen(self):
        self.seen = True

class UserMessage(BasicMessage, UserMessageMapper):

    def __init__(self, mid, text, sender, receiver):
        super(self.__class__, self).__init__(mid, text, sender)
        self.receiver = receiver
        self.type = "user"
        self.seen = False

class TeamMessage(BasicMessage, TeamMessageMapper):

    def __init__(self, mid, text, sender, team):
        super(self.__class__, self).__init__(mid, text, sender)
        self.team = team
        self.type = "team"