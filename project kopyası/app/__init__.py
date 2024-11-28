
from flask import Flask
from .config import load_secrets
from .routes import main
from .healthcheck import health

def create_app():
    app = Flask(__name__)

    # Azure Key Vault'tan sırları yükle
    app.config.update(load_secrets())

    # Blueprint'leri kaydet
    app.register_blueprint(main)
    app.register_blueprint(health, url_prefix='/health')

    return app
