from project import db
from project.models.base_model import BaseModel


class Totals(BaseModel):
    __tablename__ = "totals"

    total_registries_per_category = db.Column(db.Integer)
    total_registries_per_source = db.Column(db.Integer)
    total_registries_per_category_and_province = db.Column(db.Integer)

    def __init__(
        self,
        total_registries_per_category: int = 0,
        total_registries_per_source: int = 0,
        total_registries_per_category_and_province: int = 0,
    ):
        self.total_registries_per_category = total_registries_per_category
        self.total_registries_per_source = total_registries_per_source
        self.total_registries_per_category_and_province = (
            total_registries_per_category_and_province
        )
