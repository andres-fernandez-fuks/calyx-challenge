from project import db
from sqlalchemy import func
from project.models.building import Building
from project.helpers.total_constructor import TotalConstructor
from project import logger


class TotalsController:
    '''
    Calcula los siguientes totales:
        - Registros totales por categoría de Edificio
        - Registros totales por fuente de datos
        - Registros totales por provincia y categoría de Edificio
    y los guarda en la base de datos
    '''
    @classmethod
    def calculate_totals(cls):
        logger.info("Calculando totales...")
        cls.calculate_total_registries_per_category()
        cls.calculate_total_registries_per_source()
        cls.calculate_total_registries_per_category_and_province()
        db.session.commit()
        logger.info("Totales guardados")

    @classmethod
    def add_raw_totals(cls, raw_totals, category_name):
        for raw_total in raw_totals:
            total = TotalConstructor.create_total(raw_total, category_name)
            db.session.add(total)

    @classmethod
    def calculate_total_registries_per_category(cls):
        raw_totals = (
            db.session.query(Building.category, func.count(Building.category))
            .group_by(Building.category)
            .all()
        )
        cls.add_raw_totals(raw_totals, "total_por_categoria")

    @classmethod
    def calculate_total_registries_per_source(cls):
        raw_totals = (
            db.session.query(Building.category, func.count(Building.category))
            .group_by(Building.category)
            .all()
        )
        cls.add_raw_totals(raw_totals, "total_por_fuente")

    @classmethod
    def calculate_total_registries_per_category_and_province(cls):
        raw_totals = (
            db.session.query(
                Building.category, Building.province, func.count(Building.category)
            )
            .group_by(Building.category, Building.province)
            .all()
        )
        cls.add_raw_totals(raw_totals, "total_por_categoria_y_provincia")

