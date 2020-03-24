from flask import Flask
from server.api import api_blueprint

def create_app(object_name='server.settings.DevConfig'):
    """
    An flask application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/
    Arguments:
        object_name: the python path of the config object,
                     e.g. appname.settings.ProdConfig
    """

    app = Flask(__name__)
    app.config.from_object(object_name)
    app.register_blueprint(api_blueprint, url_prefix="/api")
    return app
