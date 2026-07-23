import unittest

from app import app


class CurrencyConversionTestCase(unittest.TestCase):
    """Tests the three currency conversions required by the coursework."""

    def setUp(self):
        app.config["TESTING"] = True
        app.config["PROPAGATE_EXCEPTIONS"] = False
        self.client = app.test_client()

    def test_10_usd_to_gbp(self):
        response = self.client.post(
            "/",
            data={
                "amount": "10",
                "from_currency": "USD",
                "to_currency": "GBP",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Converted Amount: 7.9", response.data)

    def test_1_gbp_to_eur(self):
        response = self.client.post(
            "/",
            data={
                "amount": "1",
                "from_currency": "GBP",
                "to_currency": "EUR",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Converted Amount: 1.16", response.data)

    def test_23_eur_to_usd(self):
        response = self.client.post(
            "/",
            data={
                "amount": "23",
                "from_currency": "EUR",
                "to_currency": "USD",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Converted Amount: 25.07", response.data)


if __name__ == "__main__":
    unittest.main()