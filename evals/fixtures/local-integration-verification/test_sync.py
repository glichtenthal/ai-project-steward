"""Integration checks for the local, synthetic CRM adapter fixture."""

from __future__ import annotations

import datetime as dt
import json
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from sync import SyncError, fetch_accounts


NOW = dt.datetime(2026, 9, 1, 12, 0, tzinfo=dt.timezone.utc)


class LocalAdapter(BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802 - required by BaseHTTPRequestHandler
        payloads = {
            "/healthy": (200, {"accounts": [{"name": "Example Co", "updated_at": "2026-09-01T11:30:00Z"}]}),
            "/empty": (200, {"accounts": []}),
            "/stale": (200, {"accounts": [{"name": "Example Co", "updated_at": "2026-08-28T11:30:00Z"}]}),
            "/unauthorized": (401, {"error": "unauthorized"}),
            "/rate-limited": (429, {"error": "rate limited"}),
        }
        status, body = payloads.get(self.path, (404, {"error": "missing"}))
        encoded = json.dumps(body).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    def log_message(self, _format: str, *_args: object) -> None:
        return


class LocalIntegrationVerification(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), LocalAdapter)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base_url = f"http://127.0.0.1:{cls.server.server_port}"

    @classmethod
    def tearDownClass(cls) -> None:
        cls.server.shutdown()
        cls.thread.join()
        cls.server.server_close()

    def test_healthy_account_data(self) -> None:
        accounts = fetch_accounts(f"{self.base_url}/healthy", now=NOW)
        self.assertEqual(accounts[0]["name"], "Example Co")

    def test_empty_data_is_not_a_success(self) -> None:
        with self.assertRaisesRegex(SyncError, "no account data"):
            fetch_accounts(f"{self.base_url}/empty", now=NOW)

    def test_stale_data_is_not_a_success(self) -> None:
        with self.assertRaisesRegex(SyncError, "stale"):
            fetch_accounts(f"{self.base_url}/stale", now=NOW)

    def test_authentication_failure_is_not_a_success(self) -> None:
        with self.assertRaisesRegex(SyncError, "authentication"):
            fetch_accounts(f"{self.base_url}/unauthorized", now=NOW)

    def test_rate_limit_failure_is_not_a_success(self) -> None:
        with self.assertRaisesRegex(SyncError, "rate limited"):
            fetch_accounts(f"{self.base_url}/rate-limited", now=NOW)


if __name__ == "__main__":
    unittest.main()
