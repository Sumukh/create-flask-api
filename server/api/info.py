from flask_restful import Resource


class ApiInfo(Resource):
    def get(self):
        return {
            'version': '1.0',
            'example_endpoints': ['/categories']
        }
