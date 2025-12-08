import unittest
from app import app, db, MediaItem

class BasicTests(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'XNDRSOUND', response.data)
        self.assertIn(b'Official Website', response.data)

    def test_api_gallery_empty(self):
        response = self.app.get('/api/gallery')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(data), 0)

    def test_api_gallery_with_data(self):
        with app.app_context():
            item = MediaItem(
                instagram_id='test_1',
                media_type='IMAGE',
                media_url='http://example.com/test.jpg',
                permalink='http://instagram.com/test',
                caption='Test Caption'
            )
            db.session.add(item)
            db.session.commit()
        
        response = self.app.get('/api/gallery')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['caption'], 'Test Caption')

if __name__ == "__main__":
    unittest.main()
