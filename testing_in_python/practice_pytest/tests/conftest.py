# conftest.py

import pytest

@pytest.fixture(scope="module")
def slack_params():
    return {
            "slack_webhook_url": "https://hooks.slack.com...",
            "slack_alarm_name": "test alarm from config",
            "proxy_server": ""
    }
