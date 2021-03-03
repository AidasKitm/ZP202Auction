from . import db


class User(db.Model):
    __tablename__ = "User"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.VARCHAR(50), nullable=False)
    last_name = db.Column(db.VARCHAR(50), nullable=False)
    username = db.Column(db.VARCHAR(50), nullable=False, unique=True)
    password = db.Column(db.VARCHAR(50), nullable=False)
    email = db.Column(db.VARCHAR(50), nullable=False, unique=True)
    address = db.Column(db.VARCHAR(50), nullable=False)
    profile_image = db.Column(db.VARCHAR(256), nullable=True, default="default_profile_image.jpg")
    auction = db.relationship('Auction', backref="user", lazy=True)
