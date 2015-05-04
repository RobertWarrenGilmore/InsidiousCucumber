from mongoalchemy.document import Document
from mongoalchemy.fields import IntField, StringField, ListField


class Project(Document):

    config_collection_name = 'projects'

    pid = IntField()
    name = StringField()
    descr = StringField()
    url = StringField()
    teams = ListField()
    deliverables = ListField()


def __init__(self, pid, name, url, descr="No Description", teams=[], deliverables=[]):
    self.pid = pid
    self.name = name
    self.descr = descr
    self.url = url
    self.teams = teams
    self.deliverables = deliverables


def add_team(self, team_id):
    pass


def add_deliverable(self, deliv_id):
    pass