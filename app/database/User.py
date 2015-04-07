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

    def __init__(self, uid, name, email, password, message_ids):
        self.uid = uid
        self.name = name
        self.email = email
        self.message_ids = message_ids
        self.password = self.encrypt(password)
        
    def encrypt(self, password):
        #reverse password... its so secret!
        return password
    
    def check_password(self, pwd):
        return True


class Student(User):

    def __init__(self, uid, name, email, password, message_ids=[], team_ids=[], task_ids=[]):
        super(self.__class__, self).__init__(uid, name, email, password, message_ids)
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
        mongo_client.update('users',{'uid': self.uid},self.to_hashmap())

    @staticmethod  
    def get_student(uid):
        user_map = mongo_client.get_from('users',uid)
        if user_map != None:
            student_object = Student(user_map['id'], user_map['name'], user_map['email'], 
                                     user_map['team_ids'], user_map['task_ids'], user_map['message_ids'])
            return student_object

    @staticmethod  
    def get_student_by_name(name):
        user_map = mongo_client.get_from_attr('users', name)
        student_object = None

        if user_map != None:
            student_object = Student(user_map['uid'], user_map['name'], user_map['email'], 
                                     user_map['team_ids'], user_map['task_ids'], user_map['message_ids'])

        return student_object

class Instructor(User):
    
    def __init__(self, uid, name, email, password, message_ids=[]):
        super(self.__class__, self).__init__(uid, name, email, password, message_ids)
        
    def add_class(self,class_id):
        self.class_id += [class_id]
        
    def save(self):
        mongo_client.update('users',{'id': self.id},self.to_hashmap())
        
    @staticmethod  
    def get_instructor(uid):
        user_map = mongo_client.get_from('users', id)
        if user_map != None:
            user_object = Instructor(user_map['id'],user_map['name'],user_map['email'],user_map['message_ids'])
            return user_object

    @staticmethod  
    def get_instructor_by_name(name):
        user_map = mongo_client.get_from_attr('users', name)
        if user_map != None:
            user_object = Instructor(user_map['id'],user_map['name'],user_map['email'],user_map['message_ids'])
            return user_object