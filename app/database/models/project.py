from mongoalchemy.document import Document
from mongoalchemy.fields import IntField, StringField, ListField


class Project(Document):

    config_collection_name = 'projects'

    pid = IntField()
    name = StringField()
    descr = StringField()
    url = StringField()
    teams = ListField(IntField())
    deliverables = ListField(IntField())

    def __init__(self, pid, name, url, descr="No Description", teams=[], deliverables=[]):
        self.pid = pid
        self.name = name
        self.descr = descr
        self.url = url
        self.teams = teams
        self.deliverables = deliverables