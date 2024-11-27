from flask import Blueprint, jsonify
from .database import get_db_connection

main = Blueprint('main', __name__)

# Ana sayfa endpoint'i
@main.route('/', methods=['GET'])
def home():
    return jsonify({
        "status": "success",
        "message": "Ana Sayfa: Flask Uygulaması Başarıyla Çalışıyor!"
    }), 200

# Veritabanı bağlantı testi endpoint'i
@main.route('/hello', methods=['GET'])
def hello():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 'Hello, Database Connection Successful!'")
        result = cursor.fetchone()
        conn.close()
        return jsonify({
            "status": "success",
            "message": result[0]
        }), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": "Failed to connect to the database",
            "error": str(e)
        }), 500
