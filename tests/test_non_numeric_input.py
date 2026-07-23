import unittest

from app import app


class NonNumericInputTestCase(unittest.TestCase):
    """Tests the application's handling of non-numeric input."""

    def setUp(self):
        app.config["TESTING"] = True
        app.config["PROPAGATE_EXCEPTIONS"] = False
        self.client = app.test_client()

    def test_non_numeric_amount_is_handled_without_crashing(self):
        response = self.client.post(
            "/",
            data={
                "amount": "abc",
                "from_currency": "USD",
                "to_currency": "GBP",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Please enter a numeric amount.",
            response.data,
        )


if __name__ == "__main__":
    unittest.main()