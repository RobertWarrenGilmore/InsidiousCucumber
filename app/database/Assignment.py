'''
Created on Apr 6, 2015

@author: chris
'''

import mongo_client


class Assignment(object):
    id = None
    class_id = None
    due = None
    description = None
    
    def __init__(self,id,class_id,due,description):
        self.id = id
        self.class_id = class_id
        self.due = due
        self.description = description
        
    def to_hashmap(self):
        return self.__dict__
        
    def save(self):
        mongo_client.update('assignments',{'id': self.id},self.to_hashmap())


class Deliverable(Assignment):
    assigned_team = None
    
    def __init__(self,id,class_id,due,description,team):
        super(self.__class__, self).__init__(id,class_id,due,description)
        self.assigned_team = team


class Task(Assignment):
    assigned_user = None
    
    def __init__(self,id,class_id,due,description,user):
        super(self.__class__, self).__init__(id,class_id,due,description)
        self.assigned_user = user