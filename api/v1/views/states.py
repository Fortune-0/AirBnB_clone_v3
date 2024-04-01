#!/usr/bin/python3
"""Handle requests to the api for State"""

from api.v1.views import app_views
from flask import jsonify, abort
from os import environ

@app_views.route("/states/",
                 strict_slashes=False)
def return_states():
    """Return JSON object containing list of states in database"""
    from models import storage
    from models.state import State
    return_list = []
    state_dict = storage.all("State")
    for item in state_dict.values():
        return_list.append(item.to_dict())
    return jsonify(return_list)


@app_views.route("/states/<state_id>", methods=['GET'])
def return_a_state(state_id):
    """Return state in database corresponding to state_id"""
    from models import storage
    from models.state import State
    states_dict = storage.all(State)
    for item in states_dict.values():
        if item.id == state_id:
            return jsonify(item.to_dict())
    else:
        abort(404)


@app_views.route("/states/<state_id>", methods=['DELETE'])
def delete_a_state(state_id):
    """Delete a state from the database"""
    from models import storage
    from models.state import State
    states_dict = storage.all(State)
    for item in states_dict.values():
        if item.id == state_id:
            item.delete()
            storage.save()
            return (jsonify({}), 200)
    else:
        abort(404)
