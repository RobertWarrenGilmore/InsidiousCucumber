__author__ = 'Chris'

import nose
import flask_testing
import json

from flask_login import current_user

from app import create_app
from app.database.models.user import Student


class TestLogin(flask_testing.TestCase):

    def create_app(self):
        return create_app(mode='TEST')

    def setUp(self):
        self.stu = Student.init_student('test', 'user', 'test_user', 'test_password')
        self.stu.save()

    def tearDown(self):
        Student.objects(username='test_user').first().delete()

    def test_login_success(self):
        with self.client:
            response = self.client.post('/auth/login',
                                        data=json.dumps({
                                                         'username': 'test_user',
                                                         'password': 'test_password'
                                                         }),
                                        content_type='application/json'
                                        )
            self.assert_200(response)
            self.assertTrue(current_user.is_authenticated(), 'The current user is still logged in')

    def test_login_fail(self):
        with self.client:
            response = self.client.post('/auth/login',
                                        data=json.dumps({
                                                         'username': 'test_user',
                                                         'password': 'test_invalid_password'
                                                         }),
                                        content_type='application/json'
                                        )
            self.assert_404(response)
            self.assertFalse(current_user.is_authenticated(), 'The current user is still logged in')

if __name__ == '__main__':
    nose.main()