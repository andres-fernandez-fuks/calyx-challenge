import csv
from project.wrappers.requested_data import RequestedData


class DataParser:
    """
    Parsea los datos de entrada y los devuelve en un objeto RequestedData
    """
    @classmethod
    def read_data(cls, raw_data):
        return csv.DictReader(raw_data.splitlines())

    @classmethod
    def parse_data(cls, requested_data):
        museums_data = cls.read_data(requested_data.museums_data)
        cinemas_data = cls.read_data(requested_data.cinemas_data)
        libraries_data = cls.read_data(requested_data.libraries_data)
        return RequestedData(
            museums_data=museums_data,
            cinemas_data=cinemas_data,
            libraries_data=libraries_data,
        )

    @classmethod
    def parse_cinema_data(cls, cinema_raw_data):
        return cls.read_data(cinema_raw_data)
