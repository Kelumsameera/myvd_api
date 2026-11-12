"""HTTP input validation tests; no downloads or external network calls."""
import unittest
from app import app


class DownloadRequestValidationTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_missing_json_body(self):
        response = self.client.post("/download")
        self.assertEqual(response.status_code, 400)

    def test_malformed_json(self):
        response = self.client.post(
            "/download",
            data='{"url":',
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 400)

    def test_json_array(self):
        response = self.client.post("/download", json=["https://example.com"])
        self.assertEqual(response.status_code, 400)

    def test_missing_url(self):
        response = self.client.post("/download", json={})
        self.assertEqual(response.status_code, 400)

    def test_empty_url(self):
        response = self.client.post("/download", json={"url": "  "})
        self.assertEqual(response.status_code, 400)

    def test_non_string_url(self):
        response = self.client.post("/download", json={"url": 123})
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
