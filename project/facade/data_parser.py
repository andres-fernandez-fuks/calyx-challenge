import csv
from project.facade.requested_data import RequestedData


class DataParser:
    @classmethod
    def read_data(cls, raw_data):
        return csv.DictReader(raw_data.text.splitlines())

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
