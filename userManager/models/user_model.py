from userManager import db, ma
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    date_birth = db.Column(db.Date, nullable=False)
    address = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    mobile_phone = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(255), nullable=False)

    def __init__(self, id = None, first_name = None, last_name = None, date_birth = None, address = None, password = None, mobile_phone = None, email = None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.date_birth = date_birth
        self.address = address
        self.password = password
        self.mobile_phone = mobile_phone
        self.email = email

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        exclude = ('password',)

