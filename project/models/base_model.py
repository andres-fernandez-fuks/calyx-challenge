from datetime import datetime
from project import db

class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    load_date = db.Column(db.DateTime, default=datetime.utcnow)