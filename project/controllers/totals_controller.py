from project import db
from sqlalchemy import func
from project.models.building import Building
from project.helpers.total_constructor import TotalConstructor


class TotalsController:
    @classmethod
    def calculate_totals(cls):
        cls.calculate_total_registries_per_category()
        cls.calculate_total_registries_per_source()
        cls.calculate_total_registries_per_category_and_province()
        db.session.commit()

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

