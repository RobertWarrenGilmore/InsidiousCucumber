'''
Created on Apr 6, 2015

@author: chris
'''

import mongo_client

class Course():
    id = None
    name = None
    assign_id = None
    instruct_id = None
    
    def __init__(self,id,name):
        self.id = id
        self.name = name
        self.assign_id = []
        self.instruct_id = []
        
    def to_hashmap(self):
        return self.__dict__
    
    def save(self):
        mongo_client.update('classes',{'id': self.id},self.to_hashmap())
        