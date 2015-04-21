from app.database.mappers.projectMapper import ProjectMapper

class Project(ProjectMapper):
	
	def __init__(self, pid, name, description, url):
		self.id = id
		self.name = name
		self.description = description
		self.url = url
		self.teams = []
		self.deliverables = []
		
	def add_team(self,team_id):
		pass
		
	def add_deliverable(self,deliv_id):
		pass