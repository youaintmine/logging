import json

from flask import Blueprint, jsonify, request
from werkzeug.exceptions import BadRequest

from app.services.ElasticIngestService import ElasticIngester

ingest_module = Blueprint('ingest', __name__)

@ingest_module.route("/ingest_logs", methods=["POST", "GET"])
def ingest_logs():
    log_data, result= {},{}
    if request.method == "GET":
        return "Ingest logs API takes POST requests. Thank You!"
    try:
        if not request.json:
            return jsonify(json.dumps("Empty ingest Request Form")), 400
        if not request.json.get("ingest_logs"):
            return jsonify(json.dumps("Ingest Logs empty list, nothing to insert")), 400
        form_data = request.json
        ingest_logs = form_data.get("ingest_logs", [])
        ElasticIngester.insert_logs_into_es(ingest_logs)
        return jsonify("Ingestion Successful into ElasticSearch")

    except BadRequest as e:
        return jsonify(json.dumps(e.description)), 400
    except Exception as exe:
        return jsonify(json.dumps(exe))
