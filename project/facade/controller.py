from project.facade.data_parser import DataParser
from project.helpers.building_constructor import BuildingConstructor
from project import db


class Controller:
    def __init__(self, requested_data):
        self.parsed_data = DataParser.parse_data(requested_data)

    def save_data(self):
        self.add_buildings_data()
        self.calculate_cinema_data()
        self.calculate_totals()
        # db.session.commit()

    def add_buildings_data(self):
        self.create_museums()
        self.create_cinemas()
        self.create_libraries()

    def create_museums(self):
        self.create_buildings(self.parsed_data.museums_data, "museo")

    def create_cinemas(self):
        self.create_buildings(self.parsed_data.cinemas_data, "cine")

    def create_libraries(self):
        self.create_buildings(self.parsed_data.libraries_data, "biblioteca")

    def create_buildings(self, buildings_data, building_type):
        for building_data in buildings_data:
            self.create_building(building_data, building_type)
        db.session.commit()

    def create_building(self, building_data, building_type):
        building = BuildingConstructor.create_building(building_data, building_type)
        db.session.add(building)

    def calculate_totals(self):
        pass
        # totals = Totals(self.parsed_data)
        # db.session.add(totals)

    def calculate_cinema_data(self):
        pass
        # cinema_data = CinemaData(self.parsed_data)
        # db.session.add(cinema_data)

