'''
Created on Apr 6, 2015

@author: chris, Randy
'''

from app.database.models.common import CommonEqualityMixin
from app.database.mappers.messageMapper import UserMessageMapper, TeamMessageMapper


class BasicMessage(CommonEqualityMixin,object):
    
    def __init__(self, id,text,sender):
        self.id = id
        self.text = text
        self.sender = sender
        
    def mark_as_seen(self):
        self.seen = True
        self.save()


class UserMessage(BasicMessage):
    receiver = None
    
    def __init__(self,id,text,sender,receiver):
		super(self.__class__, self).__init__(id, text, sender)
		self.receiver = receiver
		self.type = "user"
		self.seen = False

class TeamMessage(BasicMessage):
    team = None
    
    def __init__(self,id,text,sender,team):
        super(self.__class__, self).__init__(id, text, sender)
        self.team = team
        self.type = "team"