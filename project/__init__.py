from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from project.facade.database_handler import DatabaseHandler

CONFIG_FILENAME = "flask.cfg"

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(CONFIG_FILENAME)
    DatabaseHandler.create_database(app)
    db.init_app(app)
    migrate.init_app(app, db)
    with app.app_context():
        DatabaseHandler.upgrade_database()
    return app
