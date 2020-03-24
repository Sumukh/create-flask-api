from flask_restful import Resource, reqparse
from services.images import (search_unsplash, get_unsplash_collection,
                             get_reddit_images)


class UnsplashSearchApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('query', required=True)
    parser.add_argument('page', type=int, required=False)

    def get(self):
        args = self.parser.parse_args()
        response = search_unsplash(args['query'], page=args['page'])
        return response


class UnsplashCategoryApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('page', required=False)

    def get(self, category_id=None):
        args = self.parser.parse_args()
        return get_unsplash_collection(
            collection_id=category_id, page=args['page'])


class RedditSearchApi(Resource):
    def get(self, subreddit):
        response = get_reddit_images(subreddit)
        return response
