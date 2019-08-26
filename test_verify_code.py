import pytest
import requests
import json

from tests.test_session import test_get_session

@pytest.mark.api
def test_get_session(test_config, test_get_session):
    print(test_get_session)
    url = test_config.get("url") + "graph-validate-code?code=" + test_get_session
    response = requests.request("GET", url, data={})
    response_content = json.loads(response.content)
    assert response.status_code == 200 and len(response_content.get("data")) == 36



@pytest.mark.api
def test_login2():
    print("22222222222222222222222")