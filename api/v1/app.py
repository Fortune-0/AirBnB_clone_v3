#!/usr/bin/python3
"""Define application as instance of Flask"""
from api.v1.views import app_views
from flask import Flask
from models import storage
from os import environ

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')


@app.teardown_appcontext
def teardown(exception=None):
    """Destroy current session at the end of request"""
    storage.close()


if __name__ == "__main__":
    app.run(host=environ.get('HBNB_API_HOST', '0.0.0.0'),
            port=environ.get('HBNB_API_PORT', 5000), threaded=True)
