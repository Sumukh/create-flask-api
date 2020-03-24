import pytest

from server import create_app

@pytest.fixture
def app():
    return create_app('test')
