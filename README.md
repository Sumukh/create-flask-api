# Create Flask API

A boilerplate Flask application on which to build APIs using best practices.

- ✅ RESTful API (with argument validation & output schemas)
- ✅ 100% Code Coverage in Tests
- ✅ Using Flask Best Practices
- ✅ Support Heroku Deployment
- ✅ With an example image API

## Installation

```bash
$ git clone
$ cd create-flask-api
$ python3 -m venv env; source env/bin/activate # To set up an virtual env
$ ./dev-server.sh # runs: FLASK_DEBUG="true" FLASK_APP="server:create_app" flask run
```

### Key Files:

The API Endpoints are defined in `server/api` and registered to specific routes in `server/api/__init__.py`.

## Testing

To test with a coverage report:

`pytest --cov-report term-missing --cov=server`

## Limitations

This repo is designed to be the barebones for an API. If you want to hook into a database or do  authentication, you should look into [Flask Ignite](https://github.com/sumukh/ignite)
