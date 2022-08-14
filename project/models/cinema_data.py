from project import db
from project.models.base_model import BaseModel


class CinemaData(BaseModel):
    __tablename__ = 'cinema_datas'

    province = db.Column(db.String(200))
    total_screens = db.Column(db.Integer)
    total_seats = db.Column(db.Integer)
    total_INCAA_spaces = db.Column(db.Integer)