"""Created on Apr 6, 2015

@author: chris
"""

from flask_login import UserMixin
from mongoengine.document import Document
from mongoengine.fields import IntField, StringField, ListField, SequenceField
from werkzeug.security import check_password_hash, generate_password_hash

from app.database.models.common import CommonEqualityMixin


class User(Document, CommonEqualityMixin, UserMixin):
    """ Base User Class. Inherited by Student and Instructor
    Contains base functionality and fields for both classes
    """

    meta = {'allow_inheritance': True,
            'collection': 'users'}

    uid = SequenceField(primary_key=True, required=True, unique=True)
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    username = StringField(required=True)
    type = StringField(required=True, max_length=1, choices=('u', 'i'))
    message_ids = ListField(IntField(), default=[])
    encrypt_pw = StringField(required=True)

    def __init__(self, *args, **kwargs):
        Document.__init__(self, *args, **kwargs)
        if 'uid' in kwargs:
            self.uid = kwargs['uid']
        if 'first_name' in kwargs:
            self.first_name = kwargs['first_name']
        if 'last_name' in kwargs:
            self.last_name = kwargs['last_name']
        if 'username' in kwargs:
            self.username = kwargs['username']
        if 'type' in kwargs:
            self.type = kwargs['type']
        if 'message_ids' in kwargs:
            self.message_ids = kwargs['message_ids']
        if 'encrypt_pw' in kwargs:
            self.encrypt_pw = kwargs['encrypt_pw']

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    def verify_password(self, password):
        return check_password_hash(self.encrypt_pw, password)

    def get_id(self):
        return self.uid


class Student(User):
    """Student in the system"""

    team_ids = ListField(IntField(), default=[])
    task_ids = ListField(IntField(), default=[])

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        if 'team_ids' in kwargs:
            self.team_ids = kwargs['team_ids']
        if 'task_ids' in kwargs:
            self.task_ids = kwargs['task_ids']

    @staticmethod
    def init_student(first_name, last_name, username, password):
        type = 'u'
        encrypt_pw = generate_password_hash(password)
        uid = User.objects.count() + 1
        return Student(uid=uid, type=type, first_name=first_name, last_name=last_name,
                       username=username, encrypt_pw=encrypt_pw)


class Instructor(User):

    class_ids = ListField(IntField(), default=[])

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        if 'class_ids' in kwargs:
            self.task_ids = kwargs['class_ids']

    @staticmethod
    def init_instructor(first_name, last_name, username, password):
        uid = User.objects.count() + 1
        type = 'u'
        encrypt_pw = generate_password_hash(password)
        return Instructor(uid=uid, type=type, first_name=first_name, last_name=last_name,
                          username=username, encrypt_pw=encrypt_pw)