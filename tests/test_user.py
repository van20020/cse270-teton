import requests
import pytest
from unittest.mock import patch

def mock_get(url, params=None, **kwargs):
    if params == {"username": "admin", "password": "admin"}:
        return MockResponse("", 401)
    elif params == {"username": "admin", "password": "qwerty"}:
        return MockResponse("", 200)
    return MockResponse("", 400)

class MockResponse:
    def __init__(self, text, status_code):  # Use __init__ instead of init
        self.text = text
        self.status_code = status_code


def test_unauthorized_access():
    url = "http://127.0.0.1:8000/users"
    params = {"username": "admin", "password": "admin"}
    with patch("requests.get", side_effect=mock_get):
        response = requests.get(url, params=params)

    assert response.status_code == 401
    assert response.text == ""  # Expecting an empty response

def test_authorized_access():
    url = "http://127.0.0.1:8000/users"
    params = {"username": "admin", "password": "qwerty"}
    with patch("requests.get", side_effect=mock_get):
        response = requests.get(url, params=params)

    assert response.status_code == 200
    assert response.text == ""  # Expecting an empty response