from mongoengine.document import Document
from mongoengine.fields import IntField, StringField, ListField, SequenceField


class Project(Document):

    meta = {'collection': 'projects'}

    pid = SequenceField(required=True, primary_key=True, unique=True)
    name = StringField(required=True)
    descr = StringField(default="No Description")
    url = StringField(default="")
    team_ids = ListField(IntField(), default=[])
    deliverable_ids = ListField(IntField(), default=[])

    def __init__(self, *args, **kwargs):
        Document.__init__(*args, **kwargs)

        if 'pid' in kwargs:
            self.pid = kwargs['pid']
        if 'name' in kwargs:
            self.name = kwargs['name']
        if 'descr' in kwargs:
            self.descr = kwargs['descr']
        if 'url' in kwargs:
            self.url = kwargs['url']
        if 'team_ids' in kwargs:
            self.team_ids = kwargs['team_ids']
        if 'deliverable_ids' in kwargs:
            self.deliverable_ids = kwargs['deliverable_ids']

    @staticmethod
    def init_project(name, url, descr, team_ids, deliverable_ids):
        pid = Project.objects.count() + 1
        return Project(pid=pid, name=name, url=url, descr=descr, team_ids=team_ids, deliverable_ids=deliverable_ids)