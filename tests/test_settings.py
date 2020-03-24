import pytest
from server.settings import DevConfig, TestConfig, ProdConfig

def test_testing_settings():
    assert DevConfig.TESTING == False
    assert ProdConfig.TESTING == False
    assert TestConfig.TESTING == True
