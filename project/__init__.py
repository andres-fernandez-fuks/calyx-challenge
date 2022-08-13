from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from project.helpers.logger import Logger

CONFIG_FILENAME = "flask.cfg"

db = SQLAlchemy()
migrate = Migrate()
logger = Logger()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(CONFIG_FILENAME)
    db.init_app(app)
    migrate.init_app(app, db)
    return app
