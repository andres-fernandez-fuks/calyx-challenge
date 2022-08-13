import os
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.exc import OperationalError
from alembic import command
from alembic.config import Config


class DatabaseHandler:
    HOST = os.getenv("POSTGRES_HOST")
    USERNAME = os.getenv("POSTGRES_USER")
    PASSWORD = os.getenv("POSTGRES_PASSWORD")
    DATABASE = os.getenv("POSTGRES_DB")
    SQLALCHEMY_DATABASE_URI = f"postgresql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}"
    ALEMBIC_CONFIG_PATH = "migrations/alembic.ini"
    alembic_cfg = Config(ALEMBIC_CONFIG_PATH)

    @classmethod
    def upgrade_database(cls):
        command.upgrade(cls.alembic_cfg, "head")

    @classmethod
    def create_database(cls, app):
        engine = create_engine(cls.SQLALCHEMY_DATABASE_URI)
        if database_exists(engine.url):
            print("La base de datos ya existe")
            return
        try:
            print("Creando base de datos...")
            create_database(engine.url)
            engine.execute(
                f"GRANT ALL PRIVILEGES ON DATABASE {cls.DATABASE} TO {cls.USERNAME}"
            )

        except OperationalError:
            pass

