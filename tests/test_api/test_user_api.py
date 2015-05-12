"""Created on Apr 20, 2015

@author: chris
"""

import unittest
import json
import nose
import flask_testing

from app import create_app
from app.database.models.user import Student, Instructor


class TestUserApi(flask_testing.TestCase):

    stu = None

    def create_app(self):
        return create_app(mode='TEST')

    def setUp(self):
        self.stu = Student.init_student('test', 'user', 'test_user', 'test_password')
        self.stu.save()

        self.inst = Instructor.init_instructor('test', 'user', 'test_user', 'test_password')
        self.inst.save()

    def tearDown(self):
        self.stu.delete()
        self.inst.delete()

    def test_get_user_auth(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = self.stu.uid
                sess['_fresh'] = True

            response = c.get('/user')

            data = json.loads(response.data)
            self.assert200(response, "A status code other than success was return")
            self.assertTrue(data['success'])

            # Test for fields
            self.assertIn('uid', data, "The uid is not present!")
            self.assertIn('first', data, "The first is not present!")
            self.assertIn('last', data, "The last is not present!")
            self.assertIn('username', data, "The username is not present!")
            self.assertIn('type', data, "The type is not present!")
            self.assertIn('courses', data, "The courses are not present!")

    def test_get_user_not_auth(self):
        with self.client as c:
            response = c.get('/user')

            self.assert401(response, "This method does not return a 401: Not Authorized status code")

    def test_get_inst_auth(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = self.inst.uid
                sess['_fresh'] = True

            response = c.get('/user')

            data = json.loads(response.data)
            self.assert200(response, "A status code other than success was return")
            self.assertTrue(data['success'])

            # Test for fields
            self.assertIn('uid', data, "The uid is not present!")
            self.assertIn('first', data, "The first is not present!")
            self.assertIn('last', data, "The last is not present!")
            self.assertIn('username', data, "The username is not present!")
            self.assertIn('type', data, "The type is not present!")
            self.assertIn('courses', data, "The courses are not present!")

    def test_post_user(self):
        with self.client as c:
            response = c.post('/user')

            self.assert405(response, "This method does not return a 405: Method Not Allowed status code")

    @unittest.skip('Not Implementing Put')
    def test_put_user(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = self.stu.uid
                sess['_fresh'] = True

            response = c.put('/user', data={'first': 'test_user_1', 'last': self.stu.last_name})

            self.assertStatus(response, 201,  "This method did not return a 201: Created ")

    def test_delete_user(self):
        with self.client as c:
            response = c.delete('/user')

            self.assert405(response, "This method does not return a 405: Method Not Allowed status code")


if __name__ == "__main__":
    nose.main()