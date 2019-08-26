import pytest
import requests
import json

@pytest.mark.parametrize('i', range(1))
@pytest.mark.api
def test_get_session(i, test_config):
    url = test_config.get("url") + "session"
    response = requests.request("GET", url, data={})
    response_content = json.loads(response.content)
    assert response.status_code == 200 and len(response_content.get("data")) == 36

