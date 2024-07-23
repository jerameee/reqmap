import unittest
from app import app, db, Requirement

class RequirementTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_requirement(self):
        response = self.app.post('/requirements', json={
            'title': 'Test Requirement',
            'description': 'This is a test.',
            'priority': 'High',
            'status': 'Open'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Requirement created successfully!', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
