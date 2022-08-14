from ..controllers.cinema_data_controller import CinemaDataController
from project.processing.data_requester import DataRequester
from project.processing.file_creator import FileCreator
from project.controllers.building_controller import BuildingController
from project.controllers.totals_controller import TotalsController
from project.processing.database_handler import DatabaseHandler
from project import logger


class Processor:
    """
    La clase "Facade" que se encarga de manejar todo el flujo de procesamiento de datos.
    """

    @staticmethod
    def start_process(app):
        try:
            logger.info("Iniciando procesamiento...")
            DatabaseHandler.create_database(app)
            requested_data = DataRequester.get_data()
            FileCreator.create_files(requested_data)
            BuildingController(requested_data).save_data()
            TotalsController.calculate_totals()
            CinemaDataController.calculate_cinema_data(requested_data.cinemas_data)
        except Exception as e:
            logger.error(e)

