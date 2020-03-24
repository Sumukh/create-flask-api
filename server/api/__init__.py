from flask import Blueprint, request
import flask_restful as restful

from server.api.info import ApiInfo
from server.api.categories import CategoriesApi
from server.api.wallpaper import (UnsplashSearchApi, UnsplashCategoryApi,
                                  RedditSearchApi)

api_blueprint = Blueprint('api', __name__)
api_blueprint.config = {}

api = restful.Api(api_blueprint)


@api_blueprint.record
def record_params(setup_state):
    """ Load used app configs into local config on registration from
    server/__init__.py """
    app = setup_state.app
    api_blueprint.config['tz'] = app.config.get('TIMEZONE', 'utc')
    api_blueprint.config['debug'] = app.debug


@api.representation('application/json')
def envelope_api(data, code, headers=None):
    """ API response envelope (for metadata/pagination).
    Optionally wraps JSON response in envelope.
    This is for successful requests only.
        data is the object returned by the API.
        code is the HTTP status code as an int
    """
    if not request.args.get('envelope'):
        return restful.representations.json.output_json(data, code, headers)
    message = 'success'
    data = {
        'data': data,
        'code': code,
        'message': message
    }
    return restful.representations.json.output_json(data, code, headers)


# If you want to version your API, you can do that by adding a prefix to
# the route here
api.add_resource(ApiInfo, '/info')
api.add_resource(CategoriesApi, '/categories')
api.add_resource(UnsplashSearchApi, '/wallpaper/unsplash/search')
api.add_resource(
    UnsplashCategoryApi,
    '/wallpaper/unsplash/category/<int:category_id>')
api.add_resource(RedditSearchApi, '/wallpaper/reddit/<string:subreddit>')
