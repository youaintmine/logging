import json
from flask import Blueprint, request, jsonify
from werkzeug.exceptions import BadRequest
from app.PostProcessing.Results import Results
from app.services.BuildQuery import BuildQuery

search_module = Blueprint('search', __name__)


@search_module.route("/search", methods=["POST", "GET"])
def search():
    log_data, result = {}, {}
    if request.method == "GET":
        return "Search_API takes POST requests. Thank You!"
    try:
        if not request.json:
            return jsonify(json.dumps("Empty Request Form")), 400
        search_query = BuildQuery.get_search_query(request.json)
        logs = Results.get_logs([search_query], "log_system")
        result = {
            "logs": logs,
            "log_count": len(logs)
        }
        return jsonify(result)

    except BadRequest as e:
        return jsonify(json.dumps(e.description)), 400
    except Exception as exe:
        return jsonify(json.dumps(exe))


