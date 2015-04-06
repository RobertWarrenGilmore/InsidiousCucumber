'''
Created on Apr 6, 2015

@author: chris
'''

import mongo_client


class Team:
    id = None
    name = None
    user_ids = None
    message_ids = None
    assign_ids = None
    meeting_ids = None
        
    def __init__(self,id,name,user_ids):
        self.id = id
        self.name = name
        self.user_ids = user_ids
        self.message_ids = []
        self.assign_ids = []
        self.meeting_ids = []
        self.save()
        
    def add_message(self, id):
        self.message_ids.insert(0,id)
        self.save()
        
    def add_assignment(self, id):
        self.assign_ids.insert(0,id)
        self.save()
        
    def add_meeting(self, id):
        self.meeting_ids.insert(0,id)
        self.save()
    
    def to_hashmap(self):
        return self.__dict__
        
    def save(self):
        mongo_client.update('teams',{'id': self.id},self.to_hashmap())
    
    @staticmethod
    def get_team(id):
        team_map = mongo_client.get_from('team',id)
        team_object = Team(team_map['id'],team_map['name'],team_map['user_ids'])
        team_object.message_ids = team_map['message_ids']
        team_object.assign_ids = team_map['assign_ids']
        team_object.meeting_ids    = team_map['meeting_ids']
        return team_object
