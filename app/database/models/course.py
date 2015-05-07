"""Created on Apr 6, 2015

@author: chris
"""

from mongoengine.document import Document
from mongoengine.fields import StringField, IntField, ListField


class Course(Document):

    config_collection_name = 'classes'

    cid = IntField()
    name = StringField()
    descr = StringField()
    proj_ids = ListField(IntField())
    assign_id = IntField()
    instruct_id = IntField()
    
    def __init__(self, cid, name, descr="No Description", proj_ids=[], assign_id=[], instruct_id=None):
        self.cid = cid
        self.name = name
        self.descr = descr
        self.proj_ids = proj_ids
        self.assign_id = assign_id
        self.instruct_id = instruct_id