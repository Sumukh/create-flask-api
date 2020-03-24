from flask_restful import Resource, fields, marshal_with, reqparse


class Category:
    def __init__(self, id, name, state='featured'):
        self.id = id
        self.name = name
        self.state = state

# Example of returning objects and using a schema to marshal out specific
# fields.

examples = [
    Category(3330448, 'nature'),
    Category(3356570, 'travel'),
    Category(1065976, 'wallpapers'),
    Category(3330445, 'patterns'),
    Category(3694365, 'gradients'),
]

class CategoriesApi(Resource):
    response_fields = {
        'name': fields.String,
        'id': fields.Integer
    }

    @marshal_with(response_fields)
    def get(self):
        return examples

    @marshal_with(response_fields)
    def post(self):
        put_parser = reqparse.RequestParser()
        put_parser.add_argument('id', type=int, required=True)
        put_parser.add_argument('name', required=True)
        args = put_parser.parse_args()
        examples.append(Category(args["id"], args["name"]))
        return examples
