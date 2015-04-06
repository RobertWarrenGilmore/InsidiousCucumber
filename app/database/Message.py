'''
Created on Apr 6, 2015

@author: chris, Randy
'''

import mongo_client


class BasicMessage(object):
    id = None
    text = None
    sender = None
    seen = False
    type = None
    
    def __init__(self, id,text,sender):
        self.id = id
        self.text = text
        self.sender = sender
        
    def mark_as_seen(self):
        self.seen = True
        self.save()

    def to_hashmap(self):
        return self.__dict__
        
    def save(self):
        mongo_client.update('messages',{'id': self.id},self.to_hashmap())


class UserMessage(BasicMessage):
    receiver = None
    
    def __init__(self,id,text,sender,receiver):
        super(self.__class__, self).__init__(id, text, sender)
        self.receiver = receiver
        self.type = "user"
        self.save()

    @staticmethod
    def get_message(id):
        message_map = mongo_client.get_from('messages',id)
        message_object = UserMessage(message_map['id'],message_map['text'],message_map['sender'],message_map['receiver'])
        message_object.seen = message_map['seen']
        return message_object


class TeamMessage(BasicMessage):
    team = None
    
    def __init__(self,id,text,sender,team):
        super(self.__class__, self).__init__(id, text, sender)
        self.team = team
        self.type = "team"
        self.save()
        
    @staticmethod
    def get_message(id):
        message_map = mongo_client.get_from('messages',id)
        message_object = TeamMessage(message_map['id'],message_map['text'],message_map['sender'],message_map['team'])
        message_object.seen = message_map['seen']
        return message_object