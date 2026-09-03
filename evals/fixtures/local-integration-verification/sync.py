"""Small local CRM-adapter client used only by the evaluation fixture."""

from __future__ import annotations

import datetime as dt
import json
from urllib.error import HTTPError
from urllib.request import urlopen


class SyncError(RuntimeError):
    """A local adapter response that should prevent a completion claim."""


def fetch_accounts(endpoint: str, *, now: dt.datetime | None = None) -> list[dict]:
    """Fetch and validate a synthetic local account response.

    The endpoint must be local to this fixture; it is never a production CRM URL.
    """

    now = now or dt.datetime.now(dt.timezone.utc)
    try:
        with urlopen(endpoint, timeout=2) as response:  # nosec B310: fixture-only URL
            payload = json.loads(response.read().decode("utf-8"))
    except HTTPError as error:
        if error.code == 401:
            raise SyncError("Local adapter rejected authentication") from error
        if error.code == 429:
            raise SyncError("Local adapter rate limited the request") from error
        raise SyncError(f"Local adapter returned HTTP {error.code}") from error

    accounts = payload.get("accounts")
    if not isinstance(accounts, list) or not accounts:
        raise SyncError("Local adapter returned no account data")

    for account in accounts:
        updated = dt.datetime.fromisoformat(account["updated_at"].replace("Z", "+00:00"))
        if now - updated > dt.timedelta(hours=24):
            raise SyncError("Local adapter returned stale account data")
    return accounts
