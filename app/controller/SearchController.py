import json
import random
import string
from enum import Enum

from flask import Blueprint, request, jsonify, make_response




search_module = Blueprint('search', __name__)




@search_module.route("/search", methods=["POST", "GET"])
def search():
    log_data, result= {},{}
    is_success = True
    if request.method == "GET":
        return "Search_API takes POST requests. Thank You!"
    try:
        if not request.json:
            return jsonify(json.dumps("Empty Request Form")), 400

    return jsonify(result)
    except BadRequest as e:
        return jsonify(json.dumps(e.description)), 400