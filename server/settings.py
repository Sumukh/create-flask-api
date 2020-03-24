import os


class BaseConfig:
    TESTING = False


class DevConfig(BaseConfig):
    SERVICE_API_KEY = os.getenv('SERVICE_API_KEY', "ABC")


class TestConfig(BaseConfig):
    TESTING = True
    SERVICE_API_KEY = os.getenv('SERVICE_API_KEY', "BDC")


class ProdConfig(BaseConfig):
    SERVICE_API_KEY = os.getenv('SERVICE_API_KEY', "DEF")
