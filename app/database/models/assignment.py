'''
Created on Apr 6, 2015

@author: chris, Randy
'''
from app.database.mappers.assignmentMapper import DeliverableMapper, TaskMapper

class Assignment(object):
    
    def __init__(self, aid, class_id, due, description):
        self.aid = id
        self.class_id = class_id
        self.due = due
        self.description = description
        
    def to_hashmap(self):
        return self.__dict__


class Deliverable(Assignment, DeliverableMapper):
    
    def __init__(self, aid, class_id, due, description, team=None):
        super(self.__class__, self).__init__(aid, class_id, due, description)
        self.assigned_team = team


class Task(Assignment, TaskMapper):
    
    def __init__(self, aid, class_id, due, description, user=None):
        super(self.__class__, self).__init__(aid, class_id, due, description)
        self.assigned_user = user