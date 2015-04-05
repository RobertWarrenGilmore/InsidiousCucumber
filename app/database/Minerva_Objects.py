import mongo_client

def get_student(id):
	student_map = mongo_client.get_from('students',id)
	student_object = Student(student_map['id'],student_map['name'],student_map['email'],student_map['team_id'])
	student_object.task_ids = student_map['task_ids']
	student_object.message_ids = student_map['message_ids']
	return student_object
	
class Student:
	id = None
	name = None
	team_id = None
	email = None
	task_ids = None
	message_ids = None
		
	def __init__(self,id,name,email,team_id):
		self.id = id
		self.name = name
		self.email = email
		self.team_id = id
		self.task_ids = []
		self.message_ids = []
		self.save()

	def add_task(self,id):
		self.task_ids.insert(0,id)
		self.save()
		
	def add_message(self,id):
		self.message_ids.insert(0,id)
		self.save()
		
	def to_hashmap(self):
		map = {}
		map['id'] = self.id
		map['name'] = self.name
		map['team_id'] = self.team_id
		map['email'] = self.email
		map['task_ids'] = self.task_ids
		map['message_ids'] = self.message_ids
		return map
		
	def save(self):
		mongo_client.update('students',{'id': self.id},self.to_hashmap())
		
def get_team(id):
	team_map = mongo_client.get_from('team',id)
	team_object = Team(team_map['id'],team_map['name'],team_map['user_ids'])
	team_object.message_ids = team_map['message_ids']
	team_object.assign_ids = team_map['assign_ids']
	team_object.meeting_ids	= team_map['meeting_ids']
	return team_object

class Team:
	id = None
	name = None
	user_ids = None
	message_ids = None
	assign_ids = None
	meeting_ids = None
		
	def __init__(self,id,name,user_ids):
		self.id = id
		self.name = name
		self.user_ids = user_ids
		self.message_ids = []
		self.assign_ids = []
		self.meeting_ids = []
		self.save()
		
	def add_message(id):
		self.message_ids.insert(0,id)
		self.save()
		
	def add_assignment(id):
		self.assign_ids.insert(0,id)
		self.save()
		
	def add_meeting(id):
		self.meeting_ids.insert(0,id)
		self.save()
	
	def to_hashmap(self):
		map = {}
		map['id'] = self.id
		map['name'] = self.name
		map['user_ids'] = self.team_id
		map['message_ids'] = self.email
		map['assign_ids'] = self.task_ids
		map['meeting_ids'] = self.message_ids
		return map
		
	def save(self):
		mongo_client.update('teams',{'id': self.id},self.to_hashmap())
		
def get_message(id):
	message_map = mongo_client.get_from('messages',id)
	message_object = None
	if(message_map['type']=='user'):
		message_object = UserMessage(message_map['id'],message_map['text'],message_map['sender'],message_map['receiver'])
		message_object.seen = message_map['seen']
	else:
		message_object = TeamMessage(message_map['id'],message_map['text'],message_map['sender'],message_map['team'])
		message_object.seen = message_map['seen']
	return message_object

class BasicMessage:
	id = None
	text = None
	sender = None
	seen = False
	type = None
	
	def mark_as_seen(self):
		self.seen = True
		self.save()
	
class UserMessage(BasicMessage):
	receiver = None
	
	def __init__(self,id,text,sender,receiver):
		self.id = id
		self.text = text
		self.sender = sender
		self.receiver = receiver
		self.type = "user"
		self.save()
		
	def to_hashmap(self):
		map = {}
		map['id'] = self.id
		map['text'] = self.text
		map['sender'] = self.sender
		map['receiver'] = self.receiver
		map['seen'] = self.seen
		map['type'] = self.type
		return map
		
	def save(self):
		mongo_client.update('messages',{'id': self.id},self.to_hashmap())
		
class TeamMessage(BasicMessage):
	team = None
	
	def __init__(self,id,text,sender,team):
		self.id = id
		self.text = text
		self.sender = sender
		self.team = team
		self.type = "team"
		self.save()
		
	def to_hashmap(self):
		map = {}
		map['id'] = self.id
		map['text'] = self.text
		map['sender'] = self.sender
		map['team'] = self.team
		map['seen'] = self.seen
		map['type'] = self.type
		return map
		
	def save(self):
		mongo_client.update('messages',{'id': self.id},self.to_hashmap())
		
class Assignment():
	id = None
	class_id = None
	due = None
	description = None
	
	def __init__(self,id,class_id,due,description):
		self.id = id
		self.class_id = class_id
		self.due = due
		self.description = description
		
	def to_hashmap(self):
		map = {}
		map['id'] = self.id
		map['class_id'] = self.class_id
		map['due'] = self.due
		map['description'] = self.description
		return map
		
	def save(self):
		mongo_client.update('assignments',{'id': self.id},self.to_hashmap())
		
class Deliverable(Assignment):
	assigned_team = None
	
	def __init__(self,id,class_id,due,description,team)
		self.id = id
		self.class_id = class_id
		self.due = due
		self.description = description
		self.assigned_team = team
		
	def to_hashmap(self):
		map = super(Assignment, self).to_hashmap()
		map['assigned_team'] = self.assigned_team
		return map
	
	def save(self):
		mongo_client.update('assignments',{'id': self.id},self.to_hashmap())
		
class Task(Assignment):
	assigned_user = None
	
	def __init__(self,id,class_id,due,description,user)
		self.id = id
		self.class_id = class_id
		self.due = due
		self.description = description
		self.assigned_user = user
		
	def to_hashmap(self):
		map = super(Assignment, self).to_hashmap()
		map['assigned_user'] = self.assigned_user
		return map
	
	def save(self):
		mongo_client.update('assignments',{'id': self.id},self.to_hashmap())
		
class Class():
	id = None
	name = None
	assign_id = None
	instruct_id = None
	
	def __init__(self,id,name):
		self.id = id
		self.name = name
		assign_id = []
		instruct_id = []
		
	def to_hashmap(self):
		map = {}
		map['id'] = self.id
		map['name'] = self.name
		map['assign_id'] = self.assign_id
		map['instruct_id'] = self.instruct_id
		return map
	
	def save(self):
		mongo_clientupdate('classes',{'id': self.id},self.to_hashmap())
		
class Instructor():
	id = None
	uid = None
	class_id = None
	name = None
	email = None
	
	def __init__(self,id,uid,name,email):
		self.id = id
		self.uid = uid
		self.name = name
		self.email = email
		self.class_id = []
		
	def add_class(self,class_id):
		self.class_id += [class_id]
		
	def to_hashmap(self):
		map = {}
		map['id'] = self.id
		map['uid'] = self.uid
		map['class_id'] = self.class_id
		map['name'] = self.name
		map['email'] = self.email
		map['class_id'] = self.class_id
		return map
		
	def save(self):
		mongo_clientupdate('instructors',{'id': self.id},self.to_hashmap())