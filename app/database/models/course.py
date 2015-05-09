"""Created on Apr 6, 2015

@author: chris
"""

from mongoengine.document import Document
from mongoengine.fields import StringField, IntField, ListField


class Course(Document):

    meta = {'collection': 'classes'}

    cid = IntField(required=True, primary_key=True, unique=True)
    name = StringField(required=True)
    descr = StringField(default="No Description")
    proj_ids = ListField(IntField(), default=[])
    assign_ids = ListField(IntField(), default=[])
    instruct_id = IntField(default=None)
    
    def __init__(self, *args, **kwargs):
        Document.__init__(self, *args, **kwargs)

        if 'cid' in kwargs:
            self.cid = kwargs['cid']
        if 'name' in kwargs:
            self.name = kwargs['name']
        if 'descr' in kwargs:
            self.descr = kwargs['descr']
        if 'proj_ids' in kwargs:
            self.proj_ids = kwargs['proj_ids']
        if 'assign_id' in kwargs:
            self.assign_id = kwargs['assign_id']
        if 'instruct_id' in kwargs:
            self.instruct_id = kwargs['instruct_id']

    @staticmethod
    def init_course(name, descr, proj_ids, assign_ids, instruct_id):
        cid = Course.objects.count() + 1
        return Course(cid=cid, name=name, descr=descr, proj_ids=proj_ids, assign_ids=assign_ids, instruct_id=instruct_id)