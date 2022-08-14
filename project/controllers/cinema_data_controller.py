import pandas as pd
from project.helpers.data_parser import DataParser
from project import db, logger
from project.models.cinema_data import CinemaData


class CinemaDataController:
    """
    Calcula información de los cines (de acuerdo a la clase CinemaData) y la guarda en la base de datos
    """

    @classmethod
    def calculate_cinema_data(cls, cinema_raw_data):
        logger.info("Calculando datos de cines...")
        cinema_total_data = list(DataParser.parse_cinema_data(cinema_raw_data))
        cinema_df = pd.DataFrame(cinema_total_data)
        cinema_df["espacio_INCAA"].replace("", 0, inplace=True)
        cinema_df["espacio_INCAA"].replace(["si", "SI"], 1, inplace=True)
        cinema_df = cinema_df.astype(
            {"Pantallas": int, "Butacas": int, "espacio_INCAA": int}
        )
        cls.process_cinema_data(cinema_df)

    @classmethod
    def process_cinema_data(cls, cinema_df):
        cinema_totals = cinema_df.groupby("Provincia")
        total_screens = cinema_totals["Pantallas"].sum()
        total_seats = cinema_totals["Butacas"].sum()
        total_INCAA_spaces = cinema_totals["espacio_INCAA"].sum()
        total_df = pd.DataFrame(
            {
                "provinces": total_screens.index,
                "total_screens": total_screens.values,
                "total_seats": total_seats.values,
                "total_INCAA_spaces": total_INCAA_spaces.values,
            }
        )
        cls.create_cinema_data(total_df)

    @classmethod
    def create_cinema_data(cls, total_df):
        for index, row in total_df.iterrows():
            cinema_data = CinemaData(
                province=row["provinces"],
                total_screens=row["total_screens"],
                total_seats=row["total_seats"],
                total_INCAA_spaces=row["total_INCAA_spaces"],
            )
            db.session.add(cinema_data)
        db.session.commit()
        logger.info("Datos de cines guardados")
