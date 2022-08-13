from project.facade.requester import Requester
from project.facade.file_creator import FileCreator
from project.facade.controller import Controller
from project.facade.database_handler import DatabaseHandler
from project import logger
class Processor:
    @staticmethod
    def start_process(app):
        try:
            DatabaseHandler.create_database(app)
            DatabaseHandler.upgrade_database()
            requested_data = Requester.get_data()
            FileCreator.create_files(requested_data)
            Controller(requested_data).save_data()
        except Exception as e:
            logger.error(e)

