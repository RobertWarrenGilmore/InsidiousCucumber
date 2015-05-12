__author__ = 'chris'

import datetime
import json
import flask_testing

from app import create_app
from app.database.models.assignment import Deliverable
from app.database.models.project import Project


class TestDeliverableApi(flask_testing.TestCase):

    deliverable = None
    project = None

    def create_app(self):
        return create_app(mode='TEST')

    def setUp(self):
        self.deliverable = Deliverable.init_deliverable(1, datetime.datetime.now(), "Get some stuff Done", 2)
        self.deliverable.save()

        self.project = Project.init_project('some project', 'project_url', 'some really cool project')
        self.project.save()

    def tearDown(self):
        self.deliverable.delete()

    def test_get_deliverables_204(self):
        uri = '/deliverables'

        with self.client as c:
            response = c.get(uri, data={'project_id': self.project.pid})

        data = json.dumps(response.data)

        self.assertStatus(response, 204)
        self.assertIn('project_id', data, "Project Id not returned")
        self.assertIn('deliverables', data, "Deliverables not returned")

    def test_get_deliverables_404(self):
        uri = '/deliverable'

        with self.client as c:
            response = c.delete(uri, data={'project_id': 0})

        self.assertStatus(response, 404)

