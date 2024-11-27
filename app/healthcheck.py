
from flask import Blueprint, jsonify
from .database import test_db_connection

health = Blueprint('health', __name__)

@health.route('/', methods=['GET'])
def health_check():
    db_status = test_db_connection()
    if db_status:
        return jsonify({
            "status": "ok",
            "database": "connected",
            "message": "Database connection is successful"
        }), 200
    else:
        return jsonify({
            "status": "error",
            "database": "disconnected",
            "message": "Database connection failed"
        }), 500
