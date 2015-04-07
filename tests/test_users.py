import sys
sys.path.insert(0, '..\InsidiousCucumber')

import unittest
from app.database.User import *

class TestUserMethods(unittest.TestCase):

	def test_create(self):
		test_student_id = 'test_student_id'
		test_name = 'test name'
		test_email = 'test@email.com'
	
		s = Student(test_student_id,test_name,test_email)
		self.assertEquals(s.id,test_student_id)
		self.assertEquals(s.name,test_name)
		self.assertEquals(s.email,test_email)
		
	def test_get(self):
		test_student_id = 'test_student_id'
		test_name = 'test name'
		test_email = 'test@email.com'
	
		s = Student.get_student(test_student_id)
		self.assertEquals(s.id,test_student_id)
		self.assertEquals(s.name,test_name)
		self.assertEquals(s.email,test_email)
		
	def test_update(self):
		test_student_id = 'test_student_id'
		test_name = 'test name'
		
		test_new_name = 'test new name'
		
		s = Student.get_student(test_student_id)
		s.name = 'test new name'
		s.save()
		
		s = Student.get_student(test_student_id)
		self.assertEquals(s.name,test_new_name)
		
	def test_add_message(self):
		test_student_id = 'test_student_id'
		test_message_id = 'test_message'
		
		s = Student.get_student(test_student_id)
		s.add_message(test_message_id)
		
		s = Student.get_student(test_student_id)
		self.assertTrue(test_message_id in s.message_ids)
		
	def test_add_task(self):
		test_student_id = 'test_student_id'
		test_task_id = 'test_task'
		
		s = Student.get_student(test_student_id)
		s.add_task(test_task_id)
		
		s = Student.get_student(test_student_id)
		self.assertTrue(test_task_id in s.task_ids)
	
		
if __name__ == '__main__':
	unittest.main()