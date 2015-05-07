"""Created on Apr 6, 2015

@author: chris
"""

from flask_login import UserMixin
from mongoengine.document import Document
from mongoengine.fields import IntField, StringField, ListField, SequenceField
from werkzeug.security import check_password_hash

from app import login
from app.database.models.common import CommonEqualityMixin


class User(Document, CommonEqualityMixin, UserMixin, object):
    """ Base User Class. Inherited by Student and Instructor
    Contains base functionality and fields for both classes
    """

    meta = {'allow_inheritance': True,
            'collection': 'users'}

    uid = SequenceField(primary_key=True, required=True)
    first_name = StringField()
    last_name = StringField()
    username = StringField()
    type = StringField(max_length=1, choices=('u', 'i'))
    message_ids = ListField(IntField(), default=[])
    password = StringField()

    def __init__(self, *args, **kwargs):
        Document.__init__(self, *args, **kwargs)
        if 'first_name' in kwargs:
            self.first_name = kwargs['first_name']
        if 'last_name' in kwargs:
            self.last_name = kwargs['last_name']
        if 'username' in kwargs:
            self.username = kwargs['username']
        if 'message_ids' in kwargs:
            self.message_ids = kwargs['message_ids']
        if 'password' in kwargs:
            self.password = kwargs['password']

        self.uid = User.objects.count() + 1

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    def verify_password(self, password):
        return check_password_hash(self.password, password)

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

        self.type = 'u'


class Instructor(User):

    class_ids = ListField(IntField(), default=[])

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        if 'class_ids' in kwargs:
            self.task_ids = kwargs['class_ids']

        self.type = 'i'

@login.user_loader
def load_user(user_id):
    """Loader used by the login manager"""
    return User.objects(uid=user_id).first()