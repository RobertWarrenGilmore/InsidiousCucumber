#import sys
#sys.path.insert(0, '..\InsidiousCucumber')

import unittest
import fudge

from pymongo.collection import Collection
from pymongo.results import InsertOneResult

from app.database.mappers import UserMapper
from app.database.mappers.userMapper import StudentMapper, InstructorMapper


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
					   .with_args({'id': 1})
					   .returns(InsertOneResult))
		
		new_stu = StudentMapper.insert({'id': 1})
		self.assertIsInstance(new_stu, InsertOneResult.__class__, "An InsertOneResult was not returned")
	
	@fudge.patch('app.database.mappers.userMapper.UserMapper')
	def test_update_student_found(self, FakeUserMapper):
		query = {'id': 'test', 'name': 'test', 'email': 'test@test.com'}
		update = {'id': 'test', 'name': 'modified', 'email': 'test@test.com'}
		
		(FakeUserMapper.provides('get_collection')
					   .returns_fake()
					   .expects('update_one')
					   .with_args(query, update)
					   .returns_fake()
					   .has_attr(matched_count=1, 
						         modified_count=1, 
								 raw_result=update))

		StudentMapper.update(query, update)
		

	@fudge.patch('app.database.mappers.userMapper.UserMapper')
	def test_update_student_not_found(self, FakeUserMapper):
		query = {'id': 'test', 'name': 'test', 'email': 'test@test.com'}
		update = {'id': 'test', 'name': 'modified', 'email': 'test@test.com'}
		
		(FakeUserMapper.provides('get_collection')
					   .returns_fake()
					   .expects('update_one')
					   .with_args(query, update)
					   .returns_fake()
					   .has_attr(matched_count=0, 
						         modified_count=0, 
								 raw_result=update))

		StudentMapper.update(query, update)


	@fudge.patch('app.database.mappers.userMapper.UserMapper')
	def test_delete_student_found(self, FakeUserMapper):
		(FakeUserMapper.provides('get_collection')
					   .returns_fake()
					   .expects('delete_one')
					   .with_args({'id': 'test'})
					   .returns_fake()
					   .has_attr(deleted_count=1))
		
		delete_result = StudentMapper.delete({'id': 'test'})
		
		self.assertTrue(delete_result, "Deleting Failed")
		
	@fudge.patch('app.database.mappers.userMapper.UserMapper')
	def test_delete_student_not_found(self, FakeUserMapper):
		(FakeUserMapper.provides('get_collection')
					   .returns_fake()
					   .expects('delete_one')
					   .with_args({'id': 'test'})
					   .returns_fake()
					   .has_attr(deleted_count=0))
		
		delete_result = StudentMapper.delete({'id': 'test'})
		
		self.assertFalse(delete_result, 'Student was deleted when they should not have been')


class TestInstructorMapperMethods(unittest.TestCase):	
	
	def setUp(self):
		unittest.TestCase.setUp(self)
	
	def tearDown(self):
		unittest.TestCase.tearDown(self)
	
	@fudge.patch('app.database.mappers.userMapper.UserMapper')
	def test_get_instructor_valid_query(self, FakeUserMapper):
		(FakeUserMapper.provides('get_collection')
						  .returns_fake()
						  .expects('find_one')
						  .with_args({'args': 1})
						  .returns({'uid': 'test', 
									'name': 'test',
									'email': 'test@test.com'
									}))
		
		student = InstructorMapper.get(query_dict={'args': 1})
		
		self.assertIsInstance(student, dict, 'Dictionary Not Returned')
	
	@fudge.patch('app.database.mappers.userMapper.UserMapper')
	def test_get_instructor_invalid_query(self, FakeUserMapper):
		(FakeUserMapper.provides('get_collection')
					   .returns_fake()
					   .expects('find_one')
					   .with_args({'args': 1})
					   .returns(None))
		
		student = InstructorMapper.get({'args': 1})
		
		self.assertEquals(student, None, 'Something other than None was returned')
	
	@fudge.patch('app.database.mappers.userMapper.UserMapper')
	def test_insert_instructor(self, FakeUserMapper):
		(FakeUserMapper.provides('get_collection')
					   .returns_fake()
					   .expects('insert_one')
					   .with_args({'id': 1})
					   .returns(InsertOneResult))
		
		new_stu = InstructorMapper.insert({'id': 1})
		self.assertIsInstance(new_stu, InsertOneResult.__class__, "An InsertOneResult was not returned")
	
	@fudge.patch('app.database.mappers.userMapper.UserMapper')
	def test_update_instructor_found(self, FakeUserMapper):
		query = {'id': 'test', 'name': 'test', 'email': 'test@test.com'}
		update = {'id': 'test', 'name': 'modified', 'email': 'test@test.com'}
		
		(FakeUserMapper.provides('get_collection')
					   .returns_fake()
					   .expects('update_one')
					   .with_args(query, update)
					   .returns_fake()
					   .has_attr(matched_count=1, 
						         modified_count=1, 
								 raw_result=update))

		InstructorMapper.update(query, update)
		

	@fudge.patch('app.database.mappers.userMapper.UserMapper')
	def test_update_instructor_not_found(self, FakeUserMapper):
		query = {'id': 'test', 'name': 'test', 'email': 'test@test.com'}
		update = {'id': 'test', 'name': 'modified', 'email': 'test@test.com'}
		
		(FakeUserMapper.provides('get_collection')
					   .returns_fake()
					   .expects('update_one')
					   .with_args(query, update)
					   .returns_fake()
					   .has_attr(matched_count=0, 
						         modified_count=0, 
								 raw_result=update))

		InstructorMapper.update(query, update)


	@fudge.patch('app.database.mappers.userMapper.UserMapper')
	def test_delete_instructor_found(self, FakeUserMapper):
		(FakeUserMapper.provides('get_collection')
					   .returns_fake()
					   .expects('delete_one')
					   .with_args({'id': 'test'})
					   .returns_fake()
					   .has_attr(deleted_count=1))
		
		delete_result = InstructorMapper.delete({'id': 'test'})
		
		self.assertTrue(delete_result, "Deleting Failed")
		
	@fudge.patch('app.database.mappers.userMapper.UserMapper')
	def test_delete_instructor_not_found(self, FakeUserMapper):
		(FakeUserMapper.provides('get_collection')
					   .returns_fake()
					   .expects('delete_one')
					   .with_args({'id': 'test'})
					   .returns_fake()
					   .has_attr(deleted_count=0))
		
		delete_result = InstructorMapper.delete({'id': 'test'})
		
		self.assertFalse(delete_result, 'Student was deleted when they should not have been')

if __name__ == '__main__':
	unittest.main()