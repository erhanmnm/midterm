
import psycopg2
from flask import current_app

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=current_app.config["DB_HOST"],
            database=current_app.config["DB_NAME"],
            user=current_app.config["DB_USER"],
            password=current_app.config["DB_PASSWORD"]
        )
        return conn
    except Exception as e:
        raise RuntimeError(f"Database connection failed: {str(e)}")

def test_db_connection():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        conn.close()
        return True
    except Exception:
        return False
