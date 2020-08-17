# [<img src="https://github.com/Sumukh/Ignite/raw/master/appname/static/public/ignite/ignite-icon.png" width="25"/>](logo) Create Flask API (Flask Ignite)

A boilerplate Flask application on which to build APIs using best practices. Designed to be the API only alternative for [Flask Ignite](https://github.com/Sumukh/Ignite).

![Python application](https://github.com/Sumukh/create-flask-api/workflows/Python%20application/badge.svg)


- ✅ RESTful API (with argument validation & output schemas)
- ✅ 100% Code Coverage in Tests
- ✅ Using Flask Best Practices
- ✅ Support Deployment on Heroku, Now.sh
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

* `server/api/__init__.py`
* `server/api/wallpaper.py`
* `tests/test_wallpaper_api.py`

## Testing

To test with a coverage report:

`pytest --cov-report term-missing --cov=server`

## Deployment


### Now.sh deployment

```bash
$ now
```

### Heroku Deployment

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Limitations

This repo is designed to be the barebone setup for an API. If you want to hook into a database or do  authentication, you should look into [Flask Ignite](https://github.com/sumukh/ignite)
