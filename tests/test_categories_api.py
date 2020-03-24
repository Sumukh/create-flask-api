import pytest
import random

def test_categories_endpoint(client):
    response = client.get('/api/categories')
    assert response.status_code == 200
    data = response.json
    assert len(data) > 0
    assert data[0]['id'] is not None
    assert data[0]['name'] is not None

def test_categories_post(client):
    random_id = random.randint(2000, 5000)
    response = client.post('/api/categories', data={'id': random_id, 'name': 'Test Category'})
    assert response.status_code == 200
    data = response.json
    assert len(data) > 0
    assert data[-1]['id'] == random_id
    assert data[-1]['name'] ==  'Test Category'

