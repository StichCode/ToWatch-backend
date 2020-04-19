from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True, comment='Логин пользователя')
    email = db.Column(db.String(64), index=True, unique=True, comment='Почтовый ящик')
    password = db.Column(db.String(365), comment='Пароль(хэш)')


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128), unique=True)


class Films(db.Model):
    __tablename__ = 'films'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    english_title = db.Column(db.String)
    original_title = db.Column(db.String)
    image_path = db.Column(db.String)
    release_date = db.Column(db.Date)
    country = db.Column(db.String)
    producer = db.Column(db.String)
    scenario = db.Column(db.String)

    category = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)  # Foreign key