#!/usr/bin/python3
"""New file, purpose yet to be found"""

from flask import jsonify
from api.v1.views import app_views


@app_views.route("/status")
def return_json():
    """Return message in json format"""
    return (jsonify({"status": "OK"}))
