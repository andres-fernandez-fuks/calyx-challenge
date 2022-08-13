from project import db


class Building(db.Model):
    __tablename__ = "buildings"

    id = db.Column(db.Integer, primary_key=True)
    location_code = db.Column(db.Integer)
    province_id = db.Column(db.Integer)
    department_id = db.Column(db.Integer)
    category = db.Column(db.String(20))
    province = db.Column(db.String(200))
    location = db.Column(db.String(200))
    name = db.Column(db.String(200))
    address = db.Column(db.String(200))
    zip_code = db.Column(db.String(200))
    phone = db.Column(db.String(200))
    email = db.Column(db.String(200))
    website = db.Column(db.String(200))

    def __init__(
        self,
        location_code: int = None,
        province_id: int = None,
        department_id: int = None,
        category: str = None,
        province: str = None,
        location: str = None,
        name: str = None,
        address: str = None,
        zip_code: str = None,
        phone: str = None,
        email: str = None,
        website: str = None,
    ):
        self.location_code = location_code
        self.province_id = province_id
        self.department_id = department_id
        self.category = category
        self.province = province
        self.location = location
        self.name = name
        self.address = address
        self.zip_code = zip_code
        self.phone = phone
        self.email = email
        self.website = website

