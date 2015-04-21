'''
Created on Apr 12, 2015

@author: chris
'''
import unittest
from app.database.models import Student

class TestUserMethods(unittest.TestCase):

    def setUp(self):
        self.test_student_id = 'test_student_id'
        self.test_fname = 'test'
        self.test_lname = 'name'
        self.test_email = 'test@email.com'
        self.password = "password"
        self.stu = Student(self.test_student_id, self.test_fname, self.test_lname, self.test_email, self.password)

    def test_password_encrypt(self):
        pass
    
    def test_check_password_success(self):
        pass
    
    def test_check_password_fail(self):
        pass
    
    def test_equality(self):
        stu1 = Student('test', 'test', 'name', 'test@test.com', 'password')
        stu2 = Student('test', 'test', 'name', 'test@test.com', 'password')
        
        self.assertEqual(stu1, stu2, 'Students are not equal but they should be')
    
    def test_inequality(self):
        stu1 = Student('test', 'test', 'name', 'test@test.com', 'password')
        stu2 = Student('different', 'test', 'name', 'test@test.com', 'password')
        
        self.assertNotEqual(stu1, stu2, 'Students are equal but they should not be')

class TestStudentMethods(unittest.TestCase):
    
    def test_parse_doc(self):
        pass
    
class TestInstructorMethods(unittest.TestCase):
    pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()