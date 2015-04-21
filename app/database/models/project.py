from app.database.mappers.projectMapper import ProjectMapper

class Project(ProjectMapper):
	
	def __init__(self, pid, name, url, descr="No Description", teams=[], deliverables=[]):
		self.pid = pid
		self.name = name
		self.descr = descr
		self.url = url
		self.teams = teams
		self.deliverables = deliverables
		
	def add_team(self,team_id):
		pass
		
	def add_deliverable(self,deliv_id):
		pass