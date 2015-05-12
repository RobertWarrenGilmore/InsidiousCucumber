import unittest
import json
import nose
import flask_testing

from flask_login import login_user, current_user

from app import create_app
from app.database.models.course import Course

class TestCourseApi(flask_testing.TestCase):
	cour = None

	def create_app(self):
		return create_app(mode='TEST')

	def setUp(self):
		self.cour = Course.init_course('Test name','Test Desc',[],[],1)
		self.cour.save()
		
	def tearDown(self):
		pass
	
	def test_get_course(self):
		with self.client as c:
			response = c.get('/course/'+str(self.cour.cid))
		
		print(response)
		data = json.loads(response.data)
		self.assert200(response, "A status code other than success was return")
		
		# Test for fields
		self.assertIn('course_id', data, "The cid is not present!")
		self.assertIn('name', data, "The name is not present!")
		self.assertIn('description', data, "The desc is not present!")
		self.assertIn('projects', data, "The project_ids are not present!")
		
	def test_create_course(self):
		with self.client as c:
			data = {}
			data['name'] = 'SWEN-169'
			data['desc'] = 'Do some crazy stuff.'
			data['instructor'] = 0
			response = c.post('/course',data)
		self.assertStatus(response,201,"Unexpected status response")
		
if __name__ == "__main__":
    nose.main()