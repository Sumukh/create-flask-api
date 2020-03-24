import pytest

def test_info_endpoint(client):
    response = client.get('/api/info')
    assert response.status_code == 200

def test_envelope(client):
    response = client.get('/api/info?envelope=1')
    assert response.status_code == 200

