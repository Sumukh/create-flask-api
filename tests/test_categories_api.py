import pytest

def test_categories_endpoint(client):
    response = client.get('/api/categories')
    assert response.status_code == 200
    data = response.json
    assert len(data) > 0
    assert data[0]['id'] is not None
    assert data[0]['name'] is not None

