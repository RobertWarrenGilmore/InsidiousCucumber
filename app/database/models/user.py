'''
Created on Apr 6, 2015

@author: chris, Randy
'''

from app.database import mongo_client
from app.database.mappers.userMapper import StudentMapper, InstructorMapper


class User(object):
    """
    Base User Class. Inherited by Student and Instructor
    Contains base functionality and fields for both classes
    """

    def __init__(self, uid, name, email, password, message_ids):
        self.uid = uid
        self.name = name
        self.email = email
        self.message_ids = message_ids
        self.password = self.encrypt(password)


    #TODO: Add Real Encryption for users stored in DB
    def encrypt(self, password):
        #reverse password... its so secret!
        return password

    #TODO: Add Real Password Checking
    def check_password(self, pwd):
        return True


class Student(User, StudentMapper):
    """
    Student in the system
    """
    def __init__(self, uid, name, email, password, message_ids=[], team_ids=[], task_ids=[]):
        super(self.__class__, self).__init__(uid, name, email, password, message_ids)
        self.team_ids = team_ids
        self.task_ids = task_ids


class Instructor(User, InstructorMapper):
    
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