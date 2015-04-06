'''
Created on Apr 6, 2015

@author: chris, Randy
'''

import mongo_client

class User(object):
    id=None
    name=None
    email=None
    uid=None
    
    def to_hashmap(self):
        return self.__dict__

    def __init__(self, uid, name, email, message_ids, course_id):
        self.uid = uid
        self.name = name
        self.email = email
        self.message_ids = message_ids
        self.course_id = id


class Student(User):

    def __init__(self, uid, name, email, team_ids=[], task_ids=[], message_ids=[]):
        super(self.__class__, self).__init__(uid, name, email, message_ids)
        self.team_ids = team_ids
        self.task_ids = task_ids
        self.save()

    def add_task(self, uid):
        self.task_ids.insert(0, uid)
        self.save()
        
    def add_message(self, uid):
        self.message_ids.insert(0, uid)
        self.save()
        
    def save(self):
        mongo_client.update('users',{'id': self.id},self.to_hashmap())

    @staticmethod  
    def get_student(uid):
        user_map = mongo_client.get_from('users',uid)
        if user_map != None:
            student_object = Student(user_map['uid'], user_map['name'], user_map['email'], 
                                     user_map['team_ids'], user_map['task_ids'], user_map['message_ids'])
            return student_object


class Instructor(User):
    class_id = None
    
    def __init__(self, uid, name, email, message_ids=[]):
        super(self.__class__, self).__init__(uid, name, email, message_ids)
        
    def add_class(self,class_id):
        self.class_id += [class_id]
        
    def save(self):
        mongo_client.update('users',{'id': self.id},self.to_hashmap())
        
    @staticmethod  
    def get_instructor(uid):
        user_map = mongo_client.get_from('users',id)
        if user_map != None:
            user_object = Instructor(user_map['id'],user_map['name'],user_map['email'],user_map['message_ids'])
            return user_object
