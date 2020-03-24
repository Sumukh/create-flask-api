import pytest

def test_reddit_endpoint(client):
    response = client.get('/api/wallpaper/reddit/wallpapers')
    assert response.status_code == 200
    data = response.json
    assert len(data) > 0
    assert data[0]['url'] is not None

def test_unsplash_search_endpoint(client):
    response = client.get('/api/wallpaper/unsplash/search?query=food')
    assert response.status_code == 200
    data = response.json
    assert len(data) > 0
    assert data[0]['url'] is not None

def test_invalid_unsplash_search_endpoint(client):
    response = client.get('/api/wallpaper/unsplash/search')
    assert response.status_code == 400
    assert b'Missing required' in response.data

def test_unsplash_category(client):
    response = client.get('/api/wallpaper/unsplash/category/3330448')
    assert response.status_code == 200
    data = response.json
    assert len(data) > 0
    assert data[0]['url'] is not None
