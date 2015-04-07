'''
Created on Apr 6, 2015

@author: chris, Randy
'''

import mongo_client


class Team:
    tid = None
    name = None
    user_ids = None
    message_ids = None
    assign_ids = None
    meeting_ids = None
        
    def __init__(self,tid,name,user_ids, message_ids=[], assign_ids=[], meeting_ids=[]):
        self.tid = tid
        self.name = name
        self.user_ids = user_ids
        self.message_ids = message_ids
        self.assign_ids = assign_ids
        self.meeting_ids = meeting_ids
        self.save()
        
    def add_message(self, tid):
        self.message_ids.insert(0,id)
        self.save()
        
    def add_assignment(self, tid):
        self.assign_ids.insert(0,tid)
        self.save()
        
    def add_meeting(self, tid):
        self.meeting_ids.insert(0,tid)
        self.save()
    
    def to_hashmap(self):
        return self.__dict__
        
    def save(self):
        mongo_client.update('teams',{'id': self.tid},self.to_hashmap())
    
    @staticmethod
    def get_team(tid):
        team_map = mongo_client.get_from('team',id)
        team_object = Team(team_map['id'],team_map['name'],team_map['user_ids'], team_map['message_ids'], team_map['assign_ids'], team_map['meeting_ids'])
        return team_object
