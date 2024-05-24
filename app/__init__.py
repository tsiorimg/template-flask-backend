from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from .config import config_by_name

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    from .routes import main
    app.register_blueprint(main)

    db.init_app(app)

    return app
