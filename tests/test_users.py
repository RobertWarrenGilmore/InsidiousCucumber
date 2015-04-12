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
		
	@fudge.patch('app.database.mappers.userMapper.mongo_client')
	def test_collection_count(self, FakeDB):
		FakeDB.has_attr(db={'users': fudge.Fake().expects('count')})
		UserMapper.get_count()

	def test_to_hashmap(self):
		userMapper = UserMapper()
		userMapper.test = 'test_value'
		userMap = userMapper.to_hashmap()

		self.assertIsInstance(userMap, dict, 'Dictionary Not Returned')
		self.assertEqual(userMap, 
						{'test': 'test_value'}, 
						'Dictionary Not Returned with test value')


class TestStudentMapperMethods(unittest.TestCase):
	
	def setUp(self):
		unittest.TestCase.setUp(self)
	
	def tearDown(self):
		unittest.TestCase.tearDown(self)
	
	@fudge.patch('app.database.mappers.userMapper.UserMapper')
	def test_get_student_valid_query(self, FakeUserMapper):
		(FakeUserMapper.provides('get_collection')
						  .returns_fake()
						  .expects('find_one')
						  .with_args({'args': 1})
						  .returns({'uid': 'test', 
									'name': 'test',
									'email': 'test@test.com'
									}))
		
		student = StudentMapper.get(query_dict={'args': 1})
		
		self.assertIsInstance(student, dict, 'Dictionary Not Returned')
	
	@fudge.patch('app.database.mappers.userMapper.UserMapper')
	def test_get_student_invalid_query(self, FakeUserMapper):
		(FakeUserMapper.provides('get_collection')
					   .returns_fake()
					   .expects('find_one')
					   .with_args({'args': 1})
					   .returns(None))
		
		student = StudentMapper.get({'args': 1})
		
		self.assertEquals(student, None, 'Something other than None was returned')
	
	@fudge.patch('app.database.mappers.userMapper.UserMapper')
	def test_insert_student(self, FakeUserMapper):
		(FakeUserMapper.provides('get_collection')
					   .returns_fake()
					   .expects('insert_one')
					   .with_args({'args': 1})
					   .returns(InsertOneResult))
		
		new_stu = StudentMapper.insert({'id': 1})
		
		self.assertIsInstance(new_stu, InsertOneResult, "An InsertOneResult was not returned")
	
	@fudge.patch('app.database.mappers.userMapper.UserMapper')
	def test_update_user_user_found(self, FakeUserMapper):
		query = {'id': 'test', 'name': 'test', 'email': 'test@test.com'}
		update = {'id': 'test', 'name': 'modified', 'email': 'test@test.com'}
		
		(FakeUserMapper.provides('get_collection')
					   .returns_fake()
					   .expects('update_one')
					   .with_args(update)
					   .returns_fake()
					   .has_attr(matched_count=1, 
						         modified_count=1, 
								 raw_result=update))

		update_status = Student.update(query, update)
		
		fudge.verify()
		self.assertIsInstance(update_status, Student, 'Student Object was not returned')
		self.assertDictNotEqual(update_status.__dict__, query, 'The student was not updated')
		

	@fudge.patch('app.database.mappers.userMapper.UserMapper')
	def test_update_user_not_found(self, FakeUserMapper):
		query = {'id': 'test', 'name': 'test', 'email': 'test@test.com'}
		update = {'id': 'test', 'name': 'modified', 'email': 'test@test.com'}
		
		(FakeUserMapper.provides('get_collection')
					   .returns_fake()
					   .expects('update_one')
					   .with_args(update)
					   .returns_fake()
					   .has_attr(matched_count=0, 
						         modified_count=0, 
								 raw_result=update))

		update_status = Student.update(query, update)
		
		fudge.verify()
		self.assertEquals(update_status, None, 'An object was found when it should\'nt have')
	
	@fudge.patch('app.database.mappers.userMapper.UserMapper')
	def test_delete_user_found(self, FakeUserMapper):
		(FakeUserMapper.provides('get_collection')
					   .returns_fake()
					   .expects('delete_one')
					   .with_args({'id': 'test'})
					   .returns_fake()
					   .has_attr(deleted_count=1))
		
		delete_result = Student.delete({'id': 'test'})
		
		fudge.verify()
		self.assertTrue(delete_result, "Deleting Failed")
		
	@fudge.patch('app.database.mappers.userMapper.UserMapper')
	def test_delete_user_not_found(self, FakeUserMapper):
		(FakeUserMapper.provides('get_collection')
					   .returns_fake()
					   .expects('delete_one')
					   .with_args({'id': 'test'})
					   .returns_fake()
					   .has_attr(deleted_count=0))
		
		delete_result = Student.delete({'id': 'test'})
		
		fudge.verify()
		self.assertFalse(delete_result, 'Student was deleted when they should not have been')
		
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
	
	def test_equality(self):
		stu1 = Student('test', 'test', 'test@test.com', 'password')
		stu2 = Student('test', 'test', 'test@test.com', 'password')
		
		self.assertEqual(stu1, stu2, 'Students are not equal but they should be')
	
	def test_inequality(self):
		stu1 = Student('test', 'test', 'test@test.com', 'password')
		stu2 = Student('different', 'test', 'test@test.com', 'password')
		
		self.assertNotEqual(stu1, stu2, 'Students are equal but they should not be')


if __name__ == '__main__':
	unittest.main()