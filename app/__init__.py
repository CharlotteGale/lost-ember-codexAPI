from sys import prefix

from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes.codex import codex_bp
    app.register_blueprint(codex_bp, url_prefix="/codex")

    return app