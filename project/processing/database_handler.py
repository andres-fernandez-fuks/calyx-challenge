from decouple import config
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from alembic import command
from alembic.config import Config
from project import db, logger


class DatabaseHandler:
    """
    Se encarga de crear la Base de Datos (si no existe) y de actualizarla de ser necesario.
    """

    HOST = config("POSTGRES_HOST")
    USERNAME = config("POSTGRES_USER")
    PASSWORD = config("POSTGRES_PASSWORD")
    DATABASE = config("POSTGRES_DB")
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}"
    )
    ALEMBIC_CONFIG_PATH = "migrations/alembic.ini"
    alembic_cfg = Config(ALEMBIC_CONFIG_PATH)
    engine = create_engine(SQLALCHEMY_DATABASE_URI)

    @classmethod
    def should_create_database(cls):
        """
        Verifica si la base de datos existe
        """
        creation_enabled = config("ENABLE_DATABASE_CREATION", default=False, cast=bool)
        engine = create_engine(cls.SQLALCHEMY_DATABASE_URI)
        return creation_enabled and database_exists(engine.url)

    @classmethod
    def upgrade_database(cls):
        logger.info("Actualizando base de datos...")
        command.upgrade(cls.alembic_cfg, "head")
        logger.info("Base de datos actualizada")

    @classmethod
    def create_database(cls, app):
        """
        Si la base de datos no existe, la crea y la actualiza para crear las tablas.
        Si existe, borra la información de las tablas.
        """

        if cls.should_create_database():
            logger.info("La base de datos ya existe")
            cls.clear_database(app)
            return

        logger.info("Creando base de datos...")

        create_database(cls.engine.url)
        cls.engine.execute(
            f"GRANT ALL PRIVILEGES ON DATABASE {cls.DATABASE} TO {cls.USERNAME}"
        )
        cls.upgrade_database()

    @classmethod
    def clear_database(cls, app):
        logger.info("Eliminando datos de la base de datos...")
        with app.app_context():
            db.drop_all()
            cls.upgrade_database() # asegura que se creen todas las tablas, en caso de no estar actualizada la DB
            db.create_all() # solamente crea las tablas que no existen
        logger.info("Datos eliminados")
        
