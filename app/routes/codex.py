from flask import Blueprint, jsonify

codex_bp = Blueprint('codex', __name__)

@codex_bp.route('/ping')
def ping():
    return jsonify({"message": "Codex API is alive!"})

@codex_bp.route('/lineages')
def get_lineages():
    dummy = [
        {"id": 1, "name": "Highborn Faen", "description": "Elegant, mysterious..."},
        {"id": 2, "name": "Emberkin", "description": "Burning legacy in their veins..."},
    ]
    return jsonify(dummy)

