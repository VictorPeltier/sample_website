# test_happycal.py
import unittest
import os
import json
from app import create_app, db


class HappycalTestCase(unittest.TestCase):
    """This class represents the happycal test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.happycal = {'name': 'Go to Borabora for vacation'}

        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.create_all()

    def test_happycal_creation(self):
        """Test API can create a happycal (POST request)"""
        res = self.client().post('/happycals/', data=self.happycal)
        self.assertEqual(res.status_code, 201)
        self.assertIn('Go to Borabora', str(res.data))

    def test_api_can_get_all_happycals(self):
        """Test API can get a happycal (GET request)."""
        res = self.client().post('/happycals/', data=self.happycal)
        self.assertEqual(res.status_code, 201)
        res = self.client().get('/happycals/')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Go to Borabora', str(res.data))

    def test_api_can_get_happycal_by_id(self):
        """Test API can get a single happycal by using it's id."""
        rv = self.client().post('/happycals/', data=self.happycal)
        self.assertEqual(rv.status_code, 201)
        result_in_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
        result = self.client().get(
            '/happycals/{}'.format(result_in_json['id']))
        self.assertEqual(result.status_code, 200)
        self.assertIn('Go to Borabora', str(result.data))

    def test_happycal_can_be_edited(self):
        """Test API can edit an existing happycal. (PUT request)"""
        rv = self.client().post(
            '/happycals/',
            data={'name': 'Eat, pray and love'})
        self.assertEqual(rv.status_code, 201)
        rv = self.client().put(
            '/happycals/1',
            data={
                "name": "Dont just eat, but also pray and love :-)"
            })
        self.assertEqual(rv.status_code, 200)
        results = self.client().get('/happycals/1')
        self.assertIn('Dont just eat', str(results.data))

    def test_happycal_deletion(self):
        """Test API can delete an existing happycal. (DELETE request)."""
        rv = self.client().post(
            '/happycals/',
            data={'name': 'Eat, pray and love'})
        self.assertEqual(rv.status_code, 201)
        res = self.client().delete('/happycals/1')
        self.assertEqual(res.status_code, 200)
        # Test to see if it exists, should return a 404
        result = self.client().get('/happycals/1')
        self.assertEqual(result.status_code, 404)

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
