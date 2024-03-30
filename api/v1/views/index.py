#!/usr/bin/python3
"""New file, purpose yet to be found"""

from api.v1.views import app_views
from Flask import jsonify


@app_views.route("/status")
def return_json():
    """Return message in json format"""
    dic_to_json = {"status": "OK"}
    return (jsonify.dic_to_json)
