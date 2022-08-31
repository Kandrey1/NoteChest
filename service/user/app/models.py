import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import create_access_token
from passlib.hash import bcrypt

ma = Marshmallow()
db = SQLAlchemy()


class User(db.Model):
    """ Таблица пользователей """
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(250), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    create = db.Column(db.DateTime, default=datetime.datetime.today())

    def __init__(self, login, email, password):
        self.login = login
        self.email = email
        self.password = self.get_hash_pass(password)

    @classmethod
    def get_hash_pass(cls, password):
        return bcrypt.hash(password)

    def __repr__(self):
        return f"<{self.login} - {self.email} - {self.create}>"

    def get_token(self, expire_time=6) -> str:
        """ Возвращает токен пользователя
            :param
                expire_time - время действие токена в часах.
            :return
                token - токен авторизованного пользователя.
        """
        expire_delta = datetime.timedelta(expire_time)
        token = create_access_token(identity=self.id,
                                    expires_delta=expire_delta)
        return token

    @classmethod
    def authenticate(cls, email: str, password: str) -> object:
        """ Проверяет есть ли пользователь с email и password в БД.
            :param
                email - email, который необходимо проверить.
                password - пароль, который необходимо проверить.
            :return
                Объект User(содержащий информацию пользователя) из БД.
                Или Ошибку если пользователя нет или неправильный пароль.
        """
        user = cls.query.filter(cls.email == email).first()
        if not user or not bcrypt.verify(password, user.password):
            raise Exception('Incorrect email or password')
        return user


class UserSchema(ma.Schema):
    class Meta:
        model = User
        fields = ('id', 'create', 'login', 'email')
