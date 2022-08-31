from flask import request
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity
from .utils import Database
from .models import User, UserSchema


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
                raise Exception(f"User with email: {data_json['email']} exist")

            new_user = User(login=data_json['login'],
                            email=data_json['email'],
                            password=data_json['password'])

            Database.save(new_user)

            token = new_user.get_token()

        except Exception as e:
            return {'Error': f'{e}'}, 400

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
            return {'Error': f'{e}'}, 400

        return {'access_token': token}, 200


# TODO Реализовать выход пользователя
class ControllersUserLogout(Resource):
    """ Logout пользователя """
    def post(self):
        current_user = get_jwt_identity()
        return current_user, 200


class ControllersUserCrud(Resource):
    """ Обрабатывает запросы(PUT, DELETE) связанные с пользователем """
    def put(self):
        """ PUT запрос на обновление данных пользователя.
            Данные запроса передаются в json
            {"id_update":, "name":, "email":, "password":}
            :param
                id_update - id пользователя в БД, данные которого надо обновить
                name - имя пользователя.
                email - почта пользователя.
                password - пароль пользователя.
            :return Сообщение об успешности выполнения или ошибка.
        """
        try:
            data_json = request.get_json()
            # TODO обновить данные может только админ или сам пользователь
            Database.update(data_response=data_json)

        except KeyError as e:
            return {'Error': f'Не задано <{e}>'}, 400
        except Exception as e:
            return {'Error': f'{e}'}, 400

        return {'message': f"Data user id={data_json['id_update']} update"}, 200

    def delete(self):
        """ DELETE запрос на удаление пользователя из БД.
            Данные запроса передаются в json {"id_delete":}
            :param
                id_delete - id пользователя в БД, которого надо удалить.
            :returns Сообщение об успешности выполнения или ошибка.
        """
        try:
            data_json = request.get_json()

            # TODO удалить данные может только админ или сам пользователь

            Database.dell(id_delete=data_json["id_delete"])

        except Exception as e:
            return {'Error': f'{e}'}, 400

        return {'message': f"User id={data_json['id_delete']} delete"}, 200


class ControllersUserGetAll(Resource):
    """ Обрабатывает запрос(GET) связанные с пользователями """
    def get(self):
        """ GET запрос на получение списка всех пользователей в БД
            :return Список всех пользователей.
        """
        try:
            users = User.query.all()

            all_user = dict()

            for u in users:
                all_user[u.id] = u.login

        except Exception as e:
            return {'Error': f'{e}'}, 400

        return all_user, 200


class ControllersUserGet(Resource):
    """ Обрабатывает запрос(GET) связанные с пользователем """
    def get(self):
        """ GET запрос на получение данных о пользователе.
            Данные запроса передаются "?user_id="
            :param
                user_id - id пользователя.
            :return Сообщение об успешности выполнения или ошибка.
        """
        try:
            user_sh = UserSchema(many=False)
            request_user_id = request.args.get('user_id')

            data_user = User.query.filter(User.id == request_user_id).first()

            data_user_sh = user_sh.dump(data_user)

        except Exception as e:
            return {'Error': f'{e}'}, 400

        return data_user_sh, 200


class ControllersTestWork(Resource):
    """ Проверка работоспособности сервиса """
    def get(self):
        """ GET запрос возвращает код 200. """
        return 200
