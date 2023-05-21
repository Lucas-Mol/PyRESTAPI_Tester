import requests
import json
import pytest

with open('endpoints.json') as f:
    data = json.load(f)
    endpoints = data['endpoints']

@pytest.mark.parametrize('endpoint', endpoints)
def test_rest_api_is_online(endpoint):
    if endpoint.get('username'):
        payload = {
            'username': endpoint.get('username'),
            'password': endpoint.get('password')
        }
        response = requests.post(endpoint.get('url'), json=payload)
    elif endpoint.get('jwtoken'):
        headers = {
            'Authorization': f'Bearer {endpoint.get("jwtoken")}'
        }
        response = requests.get(endpoint.get('url'), headers=headers)
    else:
        response = requests.get(endpoint.get('url'))
    assert response.status_code == 200
