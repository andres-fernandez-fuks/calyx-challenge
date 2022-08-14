from datetime import datetime
from project import db

class BaseModel(db.Model):
    '''
    Clase abstracta que contiene los atributos comunes a todas las entidades
    '''
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    load_date = db.Column(db.DateTime, default=datetime.utcnow)