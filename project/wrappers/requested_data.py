class RequestedData:
    """
    Es un wrapper de un diccionario, utilizado en distintos puntos del procesamiento.
    """

    def __init__(self, museums_data, cinemas_data, libraries_data):
        self.museums_data = museums_data
        self.cinemas_data = cinemas_data
        self.libraries_data = libraries_data
