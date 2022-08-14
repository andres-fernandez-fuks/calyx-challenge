from project import db
from sqlalchemy import func
from project.models.building import Building
from project.models.totals import Totals


class DataProcessingController:
    @classmethod
    def calculate_totals(cls):
        total_registries_per_category = cls.calculate_total_registries_per_category()
        total_registries_per_source = cls.calculate_total_registries_per_source()
        totaL_registries_per_category_and_province = (
            cls.calculate_total_registries_per_category_and_province()
        )
        totals = Totals(
            total_registries_per_category=total_registries_per_category,
            total_registries_per_source=total_registries_per_source,
            total_registries_per_category_and_province=totaL_registries_per_category_and_province,
        )
        db.session.add(totals)
        db.session.commit()

    @classmethod
    def calculate_total_registries_per_category(cls):
        return (
            db.session.query(Building.category, func.count(Building.category))
            .group_by(Building.category)
            .all()
        )

    @classmethod
    def calculate_total_registries_per_source(cls):
        return (
            db.session.query(Building.source, func.count(Building.category))
            .group_by(Building.category)
            .all()
        )

    @classmethod
    def calculate_total_registries_per_category_and_province(cls):
        return (
            db.session.query(
                Building.category, Building.province, func.count(Building.category)
            )
            .group_by(Building.category, Building.province)
            .all()
        )

    