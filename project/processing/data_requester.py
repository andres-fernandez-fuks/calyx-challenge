import requests
from project.wrappers.requested_data import RequestedData


class DataRequester:
    """
    Se encarga de obtener los datos de museos, cines y bibliotecas de las urls provistas.
    """

    MUSEUMS_URL = "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv"
    CINEMAS_URL = "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv"
    LIBRARIES_URL = "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv"
    REQUEST_ENCODING = "utf-8"

    @classmethod
    def get_request(cls, url):
        req = requests.get(url)
        req.encoding = cls.REQUEST_ENCODING
        return req.text

    @classmethod
    def get_museums_data(cls):
        return cls.get_request(cls.MUSEUMS_URL)

    @classmethod
    def get_cinemas_data(cls):
        return cls.get_request(cls.CINEMAS_URL)

    @classmethod
    def get_libraries_data(cls):
        return cls.get_request(cls.LIBRARIES_URL)

    @classmethod
    def get_data(cls):
        return RequestedData(
            museums_data=cls.get_museums_data(),
            cinemas_data=cls.get_cinemas_data(),
            libraries_data=cls.get_libraries_data(),
        )

