from project import db
from project.models.base_model import BaseModel


class Total(BaseModel):
    __tablename__ = "totals"

    category = db.Column(db.String(100))
    value = db.Column(db.Integer)

    def __init__(
        self,
        category: str = None,
        value: int = None,
    ):
        self.category = category
        self.value = value
