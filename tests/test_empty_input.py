import unittest

from app import app


class EmptyInputTestCase(unittest.TestCase):
    """Tests the application's handling of an empty amount."""

    def setUp(self):
        app.config["TESTING"] = True
        app.config["PROPAGATE_EXCEPTIONS"] = False
        self.client = app.test_client()

    def test_empty_amount_is_handled_without_crashing(self):
        response = self.client.post(
            "/",
            data={
                "amount": "",
                "from_currency": "USD",
                "to_currency": "GBP",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Please enter a currency amount.",
            response.data,
        )


if __name__ == "__main__":
    unittest.main()