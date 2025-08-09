import unittest
from app import create_app


class PortfolioAppTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app()
        self.client = self.app.test_client()

    def test_health(self) -> None:
        resp = self.client.get('/health')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.get_json(), {"ok": True})

    def test_index_renders(self) -> None:
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b'Projects', resp.data)

    def test_contact_get_and_post(self) -> None:
        # GET form
        resp_get = self.client.get('/contact')
        self.assertEqual(resp_get.status_code, 200)

        # POST invalid
        resp_bad = self.client.post('/contact', data={})
        self.assertEqual(resp_bad.status_code, 400)

        # POST valid
        resp_ok = self.client.post(
            '/contact',
            data={'name': 'Alice', 'email': 'alice@example.com', 'message': 'Hello!'},
            follow_redirects=False,
        )
        self.assertEqual(resp_ok.status_code, 200)
        self.assertIn(b'Thank you, Alice!', resp_ok.data)


if __name__ == '__main__':
    unittest.main(verbosity=2)


