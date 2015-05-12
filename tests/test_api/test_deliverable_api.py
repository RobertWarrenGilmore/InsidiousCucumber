__author__ = 'chris'

import datetime
import flask_testing

from app import create_app
from app.database.models.assignment import Deliverable


class TestDeliverableApi(flask_testing.TestCase):

    deliverable = None

    def create_app(self):
        return create_app(mode='TEST')

    def setUp(self):
        self.deliverable = Deliverable.init_deliverable(1, datetime.datetime.now(), "Get some stuff Done", 2)
        self.deliverable.save()

    def tearDown(self):
        self.deliverable.delete()

    def test_delete_deliverable_204(self):
        uri = '/deliverable/' + str(self.deliverable.aid)

        with self.client as c:
            response = c.delete(uri)

        self.assertStatus(response, 204)

    def test_delete_deliverable_404(self):
        uri = '/deliverable/0'

        with self.client as c:
            response = c.delete(uri)

        self.assertStatus(response, 404)

