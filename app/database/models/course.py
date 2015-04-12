'''
Created on Apr 6, 2015

@author: chris, Randy
'''

from app.database import mongo_client


class Course():
    
    def __init__(self,cid,name, assign_id=[], instruct_id=None):
        self.id = id
        self.name = name
        self.assign_id = assign_id
        self.instruct_id = instruct_id
        
    def to_hashmap(self):
        return self.__dict__
    
    def save(self):
        mongo_client.update('classes',{'id': self.id},self.to_hashmap())
    
    @staticmethod
    def get_team(cid):
        course_map = mongo_client.get_from('team', cid)
        course_object = Course(course_map['id'],course_map['name'],course_map['assign_ids'], course_map['instruct_id'])
        return course_object