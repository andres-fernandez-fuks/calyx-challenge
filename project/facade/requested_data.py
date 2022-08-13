class RequestedData:
    """
    Basically behaves like a dictionary, I was taught to avoid returning dictionaries inside the model
    """

    def __init__(self, museums_data, cinemas_data, libraries_data):
        self.museums_data = museums_data
        self.cinemas_data = cinemas_data
        self.libraries_data = libraries_data
