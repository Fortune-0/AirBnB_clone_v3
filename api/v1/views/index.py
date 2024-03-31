#!/usr/bin/python3
"""New file, purpose yet to be found"""

from api.v1.views import app_views
from flask import jsonify
import json


@app_views.route("/status")
def return_json():
    """Return message in json format"""
    dict = {"status": "OK"}
    return (jsonify(dict))
