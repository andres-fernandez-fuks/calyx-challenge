from ..controllers.cinema_data_controller import CinemaDataController
from project.facade.requester import Requester
from project.facade.file_creator import FileCreator
from project.controllers.building_controller import BuildingController
from project.controllers.totals_controller import TotalsController
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
            BuildingController(requested_data).save_data()
            TotalsController.calculate_totals()
            CinemaDataController.calculate_cinema_data(requested_data.cinemas_data)
        except Exception as e:
            logger.error(e)

