__author__ = 'Chris'

import nose
import flask_testing
import unittest

from flask import json

from app import create_app
from app.database.models.team import Team


class TestTeamApi(flask_testing.TestCase):

    def create_app(self):
        return create_app(mode='TEST')

    def setUp(self):
        self.team = Team.init_team('test_team')
        self.team.save()

    def tearDown(self):
        team = Team.objects(name='test_team').first()
        try:
            team.delete()
        except AttributeError:
            pass

    def test_get_team(self):
        uri = '/team/' + str(self.team.tid)

        with self.client as c:
            response = c.get(uri)

        data = json.loads(response.data)
        self.assert200(response, "This call does not return a 200: Success status code")

        # Test for fields
        self.assertIn('team_id', data, "The team_id is not present!")
        self.assertIn('name', data, "The name is not present!")
        self.assertIn('members', data, "The members is not present!")

    def test_get_team_404(self):
        uri = '/team/' + str(self.team.tid + 1)
        with self.client as c:
            response = c.get(uri)

        self.assert404(response)

    def test_post_team_405(self):
        uri = '/team/' + str(self.team.tid)

        with self.client:
            response = self.client.post(uri)

        self.assert405(response, "This method does not return a 405: Method Not Allowed status code")

    @unittest.skip('Not Implementing Put')
    def test_put_team_201(self):
        uri = '/team/' + str(self.team.tid)

        with self.client as c:
            response = c.put(uri)

        self.assertStatus(response, 201, "This method did not return a 201: Created ")

    @unittest.skip('Not Implementing Put')
    def test_put_team_400(self):
        uri = '/team/' + str(self.team.tid)
        with self.client as c:
            response = c.put(uri)

        self.assertStatus(response, 400, "This method did not return a 400 ")

    def test_delete_team_204(self):
        uri = '/team/' + str(self.team.tid)
        with self.client:
            response = self.client.delete(uri)
        print(response.status)
        self.assertStatus(response, 204)

if __name__ == "__main__":
    nose.main()