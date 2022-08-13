from decouple import config
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.exc import OperationalError
from alembic import command
from alembic.config import Config
from project import logger


class DatabaseHandler:
    HOST = config("POSTGRES_HOST")
    USERNAME = config("POSTGRES_USER")
    PASSWORD = config("POSTGRES_PASSWORD")
    DATABASE = config("POSTGRES_DB")
    SQLALCHEMY_DATABASE_URI = f"postgresql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}"
    ALEMBIC_CONFIG_PATH = "migrations/alembic.ini"
    alembic_cfg = Config(ALEMBIC_CONFIG_PATH)

    @classmethod
    def upgrade_database(cls):
        logger.info("Base de datos actualizada")
        command.upgrade(cls.alembic_cfg, "head")
        logger.info("Base de datos actualizada")

    @classmethod
    def create_database(cls, app):
        engine = create_engine(cls.SQLALCHEMY_DATABASE_URI)
        if database_exists(engine.url):
            logger.info("La base de datos ya existe")
            return

        logger.info("Creando base de datos...")
        create_database(engine.url)
        engine.execute(
            f"GRANT ALL PRIVILEGES ON DATABASE {cls.DATABASE} TO {cls.USERNAME}"
        )

