import enum

from app import db


# class Category(enum.Enum):
#     film = "film"
#     series = "series"
#     cartoon = "cartoon"
#     anime = "anime"
#
#
# class Category_watching(enum.Enum):
#     want = "want"
#     looked = "looked"
#     look = "look"
#     last = "last of all"
#
#
# class With_whom(enum.Enum):
#     alone = "alone"
#     girl = "with girl"
#     friend = "with friends"


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True, comment='Логин пользователя')
    email = db.Column(db.String(64), index=True, unique=True, comment='Почтовый ящик')
    password = db.Column(db.String(365), comment='Пароль(хэш)')


class Notify(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    film_id = db.Column()


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128), unique=True)


class Films(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column()
    image_path = db.Column()
    original_title = db.Column()
    english_title = db.Column()
    year = db.Column()
    country = db.Column()
    producer = db.Column()
    scenario = db.Column()

    category = db.Column()  # Foreign key


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column()


# class Watch(db.Model):
#     _id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment="id пользователя")
#     name = db.Column(db.String(128), comment="название")
#     year = db.Column(db.String(4), comment="год выхода")
#     producer = db.Column(db.String(64), comment="режисёр/продюсер")
#     image = db.Column(db.String(64), comment="картинка превью")
#     genre_film = db.Column(db.String(164), comment="жанр фильма")
#     category = db.Column(db.Enum(), comment="категория")
#     category_watching = db.Column(db.Enum(), comment="категория")
#     rating_by_user = db.Column(db.Integer, comment="рейтинг от пользователя")
#     rating_by_other = db.Column(db.Integer, comment="рейтинг из какой то системы")
#     with_who = db.Column(db.Enum(), comment="с кем посмотреть")
#     stopped = db.Column(db.String(64), comment="где остановился")
#     review_user = db.Column(db.String(256), comment="отзыва пользователя")ы