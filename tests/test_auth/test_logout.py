__author__ = 'Chris'

import nose
import flask_testing

from flask import url_for
from flask_login import login_user, current_user

from app import create_app
from app.database.models.user import Student


class TestLogout(flask_testing.TestCase):

    stu = None

    def create_app(self):
        return create_app(mode='TEST')

    def setUp(self):
        self.stu = Student.init_student('test', 'user', 'test_user', 'test_password')
        self.stu.save()

    def tearDown(self):
        Student.objects(username='test_user').first().delete()

    def test_logout_success(self):
        login_user(self.stu)

        with self.client:
            response = self.client.get('/auth/logout')
            self.assert_redirects(response, url_for('home.index'))
            self.assertFalse(current_user.is_authenticated(), 'The current user is still logged in')

if __name__ == '__main__':
    nose.main()