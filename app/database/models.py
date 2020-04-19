from app import db
from app.database.base_models import BaseModel


class User(db.Model, BaseModel):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(365))


class Category(db.Model, BaseModel):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128), unique=True)


class Films(db.Model, BaseModel):
    __tablename__ = 'film'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    english_title = db.Column(db.String)
    original_title = db.Column(db.String)
    image_path = db.Column(db.String)
    release_date = db.Column(db.Date)
    country = db.Column(db.String)
    producer = db.Column(db.String)
    scenario = db.Column(db.String)

    category = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)  # Foreign key