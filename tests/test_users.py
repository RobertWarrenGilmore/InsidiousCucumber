#import sys
#sys.path.insert(0, '..\InsidiousCucumber')

import unittest
import fudge
from pymongo.collection import Collection
from pymongo.results import InsertOneResult

from app.database.models import Student
from app.database.mappers import UserMapper
from app.database.mappers.userMapper import StudentMapper

class TestSanity(unittest.TestCase):
	def test_sanity(self):
		self.assertEqual(1+1, 2, "Somethings Not Right")

class TestUserMapperMethods(unittest.TestCase):
	

	def setUp(self):
		unittest.TestCase.setUp(self)
		
	def tearDown(self):
		unittest.TestCase.tearDown(self)

	@fudge.patch('app.database.mappers.userMapper.mongo_client')	
	def test_get_collection(self, FakeDB):
		FakeDB.has_attr(db={'users': Collection})

		self.assertEqual(StudentMapper.get_collection(), Collection)
		
	@fudge.patch('app.database.mappers.userMapper.UserMapper.get_collection')
	def test_collection_count(self, FakeUserMapperCollection):
		FakeUserMapperCollection.is_callable().returns_fake().expects('count')
		UserMapper.get_count()
		fudge.verify()

	def test_to_hashmap(self):
		userMapper = UserMapper()
		userMapper.test = 'test_value'
		userMap = userMapper.to_hashmap()

		self.assertIsInstance(userMap, dict, 'Dictionary Not Returned')
		self.assertEqual(userMap, {'test': 'test_value'}, 'Dictionary Not Returned with test value')


class TestStudentMapperMethods(unittest.TestCase):
	
	def setUp(self):
		unittest.TestCase.setUp(self)
	
	def tearDown(self):
		unittest.TestCase.tearDown(self)
	
	@fudge.patch('app.database.mappers.userMapper.UserMapper.get_collection')
	def test_get_student_valid_query(self, FakeGetCollection):
		FakeGetCollection.is_callable().returns_fake().expects('find_one').with_arg_count(1).returns({'uid': 'test', 'name': 'test', 'email': 'test@test.com'})
		student = StudentMapper.get({'args': 1})
		fudge.verify()
		
		self.assertIsInstance(student, Student, 'Student Not Returned')
	
	@fudge.patch('app.database.mappers.userMapper.UserMapper.get_collection')
	def test_get_student_invalid_query(self, FakeGetCollection):
		FakeGetCollection.is_callable().returns_fake().expects('find_one').with_arg_count(1).returns(None)
		student = StudentMapper.get({'args': 1})
		fudge.verify()
		
		self.assertIsInstance(student, None, 'Something other than None was returned')
	
	@fudge.patch('app.database.mappers.userMapper.UserMapper.get_collection')
	def test_insert_student(self, FakeGetCollection):
		FakeGetCollection.is_callable().returns_fake().expects('insert_one').with_arg_count(1).returns(InsertOneResult)
		new_stu = StudentMapper.insert(self, {'id': 1})
		fudge.verify()
		
		self.assertIsInstance(new_stu, InsertOneResult, "An InsertOneResult was not returned")
	
	@fudge.patch('app.database.mappers.userMapper.UserMapper.get_collection')
	def test_update_user_user_found(self, FakeGetCollection):
		query = {'id': 'test', 'name': 'test', 'email': 'test@test.com'}
		update = {'id': 'test', 'name': 'modified', 'email': 'test@test.com'}
		
		(FakeGetCollection.is_callable().returns_fake()
										.expects('update_one')
										.with_args(update_dict=update)
										.returns_fake()
										.has_attr(matched_count=1, 
												  modified_count=1, 
												  raw_result=update))

		update_status = Student.update(query, update)
		
		fudge.verify()
		self.assertIsInstance(update_status, Student, 'Student Object was not returned')
		self.assertDictNotEqual(update_status.__dict__, query, 'The student was not updated')
		

	@fudge.patch('app.database.mappers.userMapper.UserMapper.get_collection')
	def test_update_user_not_found(self, FakeGetCollection):
		query = {'id': 'test', 'name': 'test', 'email': 'test@test.com'}
		update = {'id': 'test', 'name': 'modified', 'email': 'test@test.com'}
		
		(FakeGetCollection.is_callable().returns_fake()
										.expects('update_one')
										.with_args(update_dict=update)
										.returns_fake()
										.has_attr(matched_count=0, 
												  modified_count=0, 
												  raw_result=query))

		update_status = Student.update(query, update)
		
		fudge.verify()
		self.assertEquals(update_status, None, 'An object was found when it should\'nt have')
	
	@fudge.patch('app.database.mappers.userMapper.UserMapper.get_collection')
	def test_delete_user_found(self, FakeGetCollection):
		(FakeGetCollection.is_callable().returns_fake()
						  				.expects('delete')
						  				.with_arg_count(1)
						  				.returns_fake()
						  				.has_attr(deleted_count=1))
		
	@fudge.patch('app.database.mappers.userMapper.UserMapper.get_collection')
	def test_delete_user_not_found(self, FakeGetCollection):
		(FakeGetCollection.is_callable().returns_fake()
						  				.expects('delete')
						  				.with_arg_count(1)
						  				.returns_fake()
						  				.has_attr(deleted_count=0))

class TestUserMethods(unittest.TestCase):

	def setUp(self):
		self.test_student_id = 'test_student_id'
		self.test_name = 'test name'
		self.test_email = 'test@email.com'
		self.password = "password"
		self.stu = Student(self.test_student_id, self.test_name, self.test_email, self.password)

	def test_password_encrypt(self):
		pass
	
	def test_check_password_success(self):
		pass
	
	def test_check_password_fail(self):
		pass
	

if __name__ == '__main__':
	unittest.main()