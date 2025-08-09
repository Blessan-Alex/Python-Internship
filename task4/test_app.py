import unittest
from typing import Any

from app import create_app


class UserApiTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app()
        self.client = self.app.test_client()

    def test_root_route(self) -> None:
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        data: Any = response.get_json()
        self.assertIn("message", data)

    def test_list_users_initially_empty(self) -> None:
        response = self.client.get("/users")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), [])

    def test_create_and_get_user(self) -> None:
        create_resp = self.client.post(
            "/users",
            json={"name": "Alice", "email": "alice@example.com"},
        )
        self.assertEqual(create_resp.status_code, 201)
        created = create_resp.get_json()
        self.assertIsInstance(created.get("id"), int)
        user_id = created["id"]

        get_resp = self.client.get(f"/users/{user_id}")
        self.assertEqual(get_resp.status_code, 200)
        self.assertEqual(get_resp.get_json()["name"], "Alice")

    def test_update_user(self) -> None:
        create_resp = self.client.post(
            "/users",
            json={"name": "Bob", "email": "bob@example.com"},
        )
        user_id = create_resp.get_json()["id"]

        update_resp = self.client.put(
            f"/users/{user_id}", json={"email": "bob+new@example.com"}
        )
        self.assertEqual(update_resp.status_code, 200)
        self.assertEqual(update_resp.get_json()["email"], "bob+new@example.com")

    def test_delete_user(self) -> None:
        create_resp = self.client.post(
            "/users",
            json={"name": "Eve", "email": "eve@example.com"},
        )
        user_id = create_resp.get_json()["id"]

        del_resp = self.client.delete(f"/users/{user_id}")
        self.assertEqual(del_resp.status_code, 204)

        get_resp = self.client.get(f"/users/{user_id}")
        self.assertEqual(get_resp.status_code, 404)


if __name__ == "__main__":
    unittest.main(verbosity=2)

