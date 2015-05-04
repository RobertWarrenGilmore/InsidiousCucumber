"""Created on Apr 6, 2015

@author: chris
"""

from flask_login import UserMixin
from mongoalchemy.document import Document
from mongoalchemy.fields import StringField, IntField, EnumField, ListField
from werkzeug.security import generate_password_hash, check_password_hash

from app import login
from app.database.models.common import CommonEqualityMixin


class User(CommonEqualityMixin, UserMixin, object):
    """ Base User Class. Inherited by Student and Instructor
    Contains base functionality and fields for both classes
    """

    config_collection_name = 'users'

    uid = IntField()
    first_name = StringField()
    last_name = StringField()
    username = StringField()
    type = EnumField()
    message_ids = ListField()
    encryptpw = StringField()

    def __init__(self, uid, first_name, last_name, username, password, utype, message_ids):
        self.uid = uid
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.type = utype
        self.message_ids = message_ids
        self.encryptpw = self.encrypt(password)

<<<<<<< HEAD
    # TODO: Add Real Encryption for users stored in DB
    def encrypt(self, password):
        # reverse password... its so secret!
        return password
=======
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.encryptpw = generate_password_hash(password)
>>>>>>> 61a75bba7a1942177eb58bb17996067bd9da5010

    def verify_password(self, password):
        return check_password_hash(self.encryptpw, password)

    def get_id(self):
        return self.uid


class Student(Document, User):
    """Student in the system"""

    def __init__(self, uid, first_name, last_name, username, password, utype='u', message_ids=[], team_ids=[],
                 task_ids=[]):
        super(self.__class__, self).__init__(uid, first_name, last_name, username, password, utype, message_ids)
        self.team_ids = team_ids
        self.task_ids = task_ids

    @staticmethod
    def parse_doc(doc):
        return Student(uid=doc['uid'],
                       first_name=doc['first_name'],
                       last_name=doc['last_name'],
                       username=doc['username'],
                       password=doc['password'],
                       utype=doc['type'],
                       message_ids=doc['message_ids'],
                       team_ids=doc['team_ids'],
                       task_ids=doc['task_ids'])


class Instructor(User):
    def __init__(self, uid, first_name, last_name, username, password, utype='p', message_ids=[], class_ids=[]):
        super(self.__class__, self).__init__(uid, first_name, last_name, username, password, utype, message_ids)
        self.class_ids = class_ids

    def add_class(self, class_id):
        self.class_id += [class_id]

    @staticmethod
    def parse_doc(doc):
        return Instructor(uid=doc['uid'],
                          first_name=doc['first_name'],
                          last_name=doc['last_name'],
                          username=doc['username'],
                          password=doc['password'],
                          utype=doc['type'],
                          message_ids=doc['message_ids'],
                          class_ids=doc['class_ids']
                          )


@login.user_loader
def load_user(user_id):
    """Loader used by the login manager"""
    if Student.get({'uid': user_id})['type'] == 'u':
        return Student.parse_doc(Student.get({'uid': user_id}))
    elif Instructor.get({'uid': user_id})['type'] == 'p':
        return Instructor.parse_doc(Instructor.get({'uid': user_id}))
    else:
        return None