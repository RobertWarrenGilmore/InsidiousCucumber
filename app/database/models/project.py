from app.database import mongo_client

class Project:
	id = None
	name = None
	description = None
	deliverables = None
	url = None
	teams = None
	
	def __init__(self,id,name,description,url):
		self.id = id
		self.name = name
		self.description = description
		self.url = url
		self.teams = []
		self.deliverables = []
		self.save()
		
	def add_team(self,team_id):
		self.teams+=[team_id]
		self.save()
		
	def add_deliverable(self,deliv_id):
		self.deliverables+=[deliv_id]
		self.save()
		
	def to_hashmap(self):
        return self.__dict__
        
    def save(self):
        mongo_client.update('projects',{'id': self.tid},self.to_hashmap())
    
    @staticmethod
    def get_project(tid):
        project_map = mongo_client.get_from('project',id)
        project_object = Project(project_map['id'],project_map['name'],project_map['description'], project_map['url'])
		project_object.deliverables = project_map['deliverables']
		project_object.teams = project_map['teams']
        return project_object