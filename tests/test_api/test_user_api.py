"""Created on Apr 20, 2015

@author: chris
"""

import nose
import flask_testing

from flask_login import login_user, current_user

from app import create_app
from app.database.models.user import Student


class TestUserApi(flask_testing.TestCase):

    def create_app(self):
        return create_app(mode='TEST')

    def setUp(self):
        self.stu = Student.init_student('test', 'user', 'test_user', 'test_password')
        self.stu.save()

    def tearDown(self):
        Student.objects(username='test_user').first().delete()

    def test_get_user_auth(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = self.stu.uid
                sess['_fresh'] = True

            response = c.get('/user')

            self.assert200(response, "A status code other than success was return")
            try:
                self.assertEqual(response.data.uid,
                                 self.stu.uid,
                                 "The uids do not match!")
            except AttributeError:
                self.fail("JSON returned did not include uid, which throws an attribute error")

            self.assertRaises(AttributeError, self.stu.password, "Password should not be visible!")

    def test_get_user_not_auth(self):
        with self.client as c:
            response = c.get('/user')

            self.assert401(response, "This method does not return a 401: Not Authorized status code")

    def test_post_user(self):
        with self.client as c:
            response = c.post('/user')

            self.assert405(response, "This method does not return a 405: Method Not Allowed status code")

    def test_put_user(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = self.stu.uid
                sess['_fresh'] = True

            response = c.put('/user')

            # self.assert200(response, "This method did not return a 201: Created ")
            # Find appropriate way of testing for 201 status code

    def test_delete_user(self):
        with self.client as c:
            response = c.delete('/user')

            self.assert405(response, "This method does not return a 405: Method Not Allowed status code")


if __name__ == "__main__":
    nose.main()