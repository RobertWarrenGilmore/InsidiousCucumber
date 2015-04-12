'''
Created on Apr 6, 2015

@author: chris
'''

from app.database.models.common import CommonEqualityMixin
from app.database.mappers.userMapper import StudentMapper, InstructorMapper


class User(CommonEqualityMixin, object):
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

    @staticmethod
    def parse_doc(doc):
        return Student(id=doc['uid'],
                       name=doc['name'],
                       email=doc['email'],
                       password=doc['password'],
                       message_ids=['message_ids'],
                       team_ids=doc['team_ids'],
                       task_ids=doc['task_ids'])

class Instructor(User, InstructorMapper):
    
    def __init__(self, uid, name, email, password, message_ids=[]):
        super(self.__class__, self).__init__(uid, name, email, password, message_ids)
        
    def add_class(self,class_id):
        self.class_id += [class_id]