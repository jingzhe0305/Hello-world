import pytest


@pytest.fixture(scope='session')
def test_config():
    _config = {
        "url": "http://192.168.16.161:8866/api/dp/v1/",  # 请求地址
    }
    return _config
