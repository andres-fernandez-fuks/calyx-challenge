from project.facade.requester import Requester
from project.facade.file_creator import FileCreator
from project.facade.controller import Controller


class Processor:
    @staticmethod
    def start_process():
        requested_data = Requester.get_data()
        FileCreator.create_files(requested_data)
        Controller(requested_data).save_data()

