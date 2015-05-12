import json
import nose
import flask_testing

from flask_login import login_user, current_user

from app import create_app
from app.database.models.project import Project


class TestUserApi(flask_testing.TestCase):

	proj = None

	def create_app(self):
		return create_app(mode='TEST')
		
	def setUp(self):
		self.proj = Project.init_project("Test Proj", "http://example.com", "Test description", [1,2], [])
		self.proj.save()

	def tearDown(self):
		Project.objects(pid=self.proj.pid).first().delete()
		
	def test_get_project(self):
		with self.client as c:
			response = c.get('/project/'+str(self.proj.pid))
				
			data = json.loads(response.data)	
				
			self.assert200(response, "A status code other than success was return")
			self.assertTrue(data['deliverables']==[])	
				
			self.assertIn('project_id', data, "The pid is not present!")	
			self.assertIn('name', data, "The name is not present!"	)
			self.assertIn('url', data, "The url is not present!")	
			self.assertIn('description', data, "The description is not pr	esent!")
			self.assertIn('team_ids', data, "The team_ids are not present!")
			self.assertIn('deliverables', data, "The deliverables are not present!")
			
	def test_post_project(self):
		with self.client as c:
			response = c.post('/project',data={'name':'Test Proj','url':'http://www.example.com','desc':'Test Description'})
			print(response)
		self.assertStatus(response,201,"Incorrect response code")
	11
if __name__ == "__main__":
    nose.main()