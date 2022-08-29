from flask import request
from flask_restful import Resource

from .utils import Database
from .models import User


class ControllersUserRegister(Resource):
    """ Регистрация пользователя """
    def post(self):
        """ POST запрос на добавление пользователя в БД.
            Данные запроса передаются в json
            {"login":, "email":, "password":}
            :param
                login - логин пользователя.
                email - почта пользователя.
                password - пароль пользователя.
            :return
                Сообщение об успешности выполнения или ошибка.
        """
        try:
            data_json = request.get_json()

            if User.query.filter(User.email == data_json['email']).first():
                raise Exception(f"Error. User with email: {data_json['email']}'\
                                'exist")

            new_user = User(login=data_json['login'],
                            email=data_json['email'],
                            password=data_json['password'])

            Database.save(new_user)

            token = new_user.get_token()

        except Exception as e:
            return {'message': f'Error. <{e}>'}

        return {'access_token': token}, 200


class ControllersUserAuth(Resource):
    """ Аутентификация пользователя """
    def post(self):
        """ POST запрос на Аутентификация пользователя.
            Данные запроса передаются в json
            {"email":, "password":}
            :param
                email - почта пользователя.
                password - пароль пользователя.
            :returns
                При успешной аутентификации возвращает токен пользователя.
                Ошибка если пользователя не существует или данные неправильные.
        """
        try:
            data_json = request.get_json()

            user = User.authenticate(email=data_json['email'],
                                     password=data_json['password'])

            token = user.get_token()

        except Exception as e:
            return {'message': f'Error. <{e}>'}

        return {'access_token': token}, 200
