'''
Created on Apr 6, 2015

@author: chris
'''

import mongo_client

class User:
    id=None
    name=None
    email=None
    uid=None
    
    def to_hashmap(self):
        return self.__dict__

class Student(User):
    team_id = None
    task_ids = None
    message_ids = None
        
    def __init__(self,id,name,email,team_id):
        self.id = id
        self.name = name
        self.email = email
        self.team_id = id
        self.task_ids = []
        self.message_ids = []
        self.save()

    def add_task(self,id):
        self.task_ids.insert(0,id)
        self.save()
        
    def add_message(self,id):
        self.message_ids.insert(0,id)
        self.save()
        
    def save(self):
        mongo_client.update('students',{'id': self.id},self.to_hashmap())
    
    @staticmethod  
    def get_student(id):
        student_map = mongo_client.get_from('students',id)
        if student_map != None:
            student_object = Student(student_map['id'],student_map['name'],student_map['email'],student_map['team_id'])
            student_object.task_ids = student_map['task_ids']
            student_object.message_ids = student_map['message_ids']
            return student_object


class Instructor(User):
    class_id = None
    
    def __init__(self,id,uid,name,email):
        self.id = id
        self.uid = uid
        self.name = name
        self.email = email
        self.class_id = []
        
    def add_class(self,class_id):
        self.class_id += [class_id]
        
    def save(self):
        mongo_client.update('instructors',{'id': self.id},self.to_hashmap())