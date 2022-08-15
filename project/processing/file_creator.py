import os
from project.helpers.date_helper import DateHelper


class FileCreator:
    """
    Guarda la información obtenida en archivos csv.
    """

    STORAGE_FOLDER = "stored_data"

    @classmethod
    def create_files(cls, requested_data):
        with open(cls.create_museums_file_path(), "w") as f:
            f.write(requested_data.museums_data)
        with open(cls.create_cinemas_file_path(), "w") as f:
            f.write(requested_data.cinemas_data)
        with open(cls.create_libraries_file_path(), "w") as f:
            f.write(requested_data.libraries_data)

    @classmethod
    def create_store_folder_if_not_exists(cls, file_folder):
        if not os.path.exists(file_folder):
            os.makedirs(file_folder)

    @classmethod
    def create_file_path(cls, category):
        full_month = DateHelper.get_full_month_from_date()
        date_folder = f"{DateHelper.now().year}-{full_month}"
        file_folder = f"{cls.STORAGE_FOLDER}/{category}/{date_folder}"
        cls.create_store_folder_if_not_exists(file_folder)
        file_name = f'{category}-{DateHelper.format_date("%d-%m-%Y")}.csv'
        file_path = f"{file_folder}/{file_name}"
        return file_path

    @classmethod
    def create_museums_file_path(cls):
        return cls.create_file_path("museos")

    @classmethod
    def create_cinemas_file_path(cls):
        return cls.create_file_path("cines")

    @classmethod
    def create_libraries_file_path(cls):
        return cls.create_file_path("bibliotecas")

