from flask_restful import Resource, fields, marshal_with

class Category:
    def __init__(self, id, name, state='featured'):
        self.id = id
        self.name = name
        self.state = state

# Example of returning objects and using a schema to marshal out specific fields
class CategoriesApi(Resource):
    get_fields = {
        'name': fields.String,
        'id': fields.Integer
    }

    @marshal_with(get_fields)
    def get(self):
        return [
            Category(3330448, 'nature'),
            Category(3356570, 'travel'),
            Category(1065976, 'wallpapers'),
            Category(3330445, 'patterns'),
            Category(3694365, 'gradients'),
        ]
