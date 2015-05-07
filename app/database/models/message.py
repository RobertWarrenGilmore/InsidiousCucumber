"""Created on Apr 6, 2015

@author: chris
"""

from mongoengine.document import Document
from mongoengine.fields import StringField, IntField, BooleanField, SequenceField

from app.database.models.common import CommonEqualityMixin


class BasicMessage(Document, CommonEqualityMixin):

    meta = {'allow_inheritance': True,
            'collection': 'messages'}

    mid = SequenceField(required=True, primary_key=True, unique=True)
    text = StringField(required=True)
    sender_id = IntField(required=True)
    seen = BooleanField(default=False)

    def __init__(self, *args, **kwargs):
        Document.__init__(*args, **kwargs)
        if 'mid' in kwargs:
            self.mid = kwargs['mid']
        if 'text' in kwargs:
            self.text = kwargs['text']
        if 'sender' in kwargs:
            self.sender = kwargs['sender']

    def mark_as_seen(self):
        self.seen = True


class UserMessage(BasicMessage):

    receiver_id = IntField(required=True)

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(self, *args, **kwargs)

        if 'receiver_id' in kwargs:
            self.receiver_id = kwargs['receiver_id']
        if 'seen' in kwargs:
            self.seen = kwargs['seen']

    @staticmethod
    def init_user_message(sender_id, receiver_id, text):
        mid = BasicMessage.objects.count() + 1
        return UserMessage(mid=mid, sender_id=sender_id, receiver_id=receiver_id, text=text)


class TeamMessage(BasicMessage):

    team_id = IntField(required=True)

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(self, *args, **kwargs)

        if 'team_id' in kwargs:
            self.team_id = kwargs['team_id']

    @staticmethod
    def init_team_message(sender_id, team_id, text):
        mid = BasicMessage.objects.count() + 1
        return UserMessage(mid=mid, sender_id=sender_id, team_id=team_id, text=text)