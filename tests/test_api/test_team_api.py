__author__ = 'Chris'

import nose
import flask_testing

from app import create_app
from app.database.models.team import Team


class TestTeamApi(flask_testing.TestCase):

    def create_app(self):
        return create_app(mode='TEST')

    def setUp(self):
        self.team = Team.init_team('test_team')
        self.team.save()

    def tearDown(self):
        Team.objects(name='test_team').first().delete()

    def test_get_team(self):
        uri = '/team/' + str(self.team.tid)

        with self.client as c:

            response = c.get(uri)

            self.assert200(response, "This call does not return a 200: Success status code")
            try:
                self.assertEqual(response.data.tid,
                                 self.team.tid,
                                 "The uid's do not match!")
            except AttributeError:
                self.fail("JSON returned did not include tid, which throws an attribute error")

    def test_get_team_404(self):
        uri = '/team/' + str(self.team.tid + 1)
        with self.client as c:

            response = c.get(uri)

            self.assert404(response, "This call does not return a 404: Not Found status code")
            try:
                self.assertEqual(response.data.uid,
                                 self.stu.uid,
                                 "The uids do not match!")
            except AttributeError:
                self.fail("JSON returned did not include uid, which throws an attribute error")

            self.assertRaises(AttributeError, self.stu.password, "Password should not be visible!")

    def test_post_team_405(self):
        uri = '/team/' + str(self.team.tid)

        with self.client:
            response = self.client.post(uri)

            self.assert405(response, "This method does not return a 405: Method Not Allowed status code")

    def test_put_team_201(self):
        uri = '/team/' + str(self.team.tid)

        with self.client as c:

            response = c.put(uri)

            self.assertStatus(response, 201, "This method did not return a 201: Created ")

    def test_put_team_404(self):
        with self.client as c:
            response = c.put('/team/1')

            self.assertStatus(response, 201, "This method did not return a 201: Created ")

    def test_delete_team_204(self):
        with self.client:
            response = self.client.delete('/team/1')

            self.assertStatus(response, 204, "This method does not return a 204: No Content status code")

if __name__ == "__main__":
    nose.main()