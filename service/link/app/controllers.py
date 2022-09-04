from flask import request
from flask_restful import Resource
from .utils import Database
from .models import Link, LinkSchema


class ControllersLinkAdd(Resource):
    """ Добавление ссылки в БД """
    def post(self):
        """ POST запрос на добавление ссылки в БД.
            Данные запроса передаются в json
            {"url":, "comment":, "user_id":}
            :param
                url - url ссылки.
                comment - комментарий к ссылке(описание).
                user_id - пользователь, кто добавил ссылку.
            :return
                Сообщение об успешности выполнения или ошибка.
        """
        try:
            data_json = request.get_json()

            if Link.query.filter(Link.url == data_json['url']).first():
                raise Exception(f"Link exist")

            new_link = Link(url=data_json['url'],
                            comment=data_json['comment'],
                            user_id=data_json['user_id'])

            Database.save(new_link)

        except Exception as e:
            return {'Error': f'{e}'}, 400

        return {'message': 'Link add'}, 200


class ControllersLinkUpdate(Resource):
    """ Обновляет данные ссылки в БД """
    def put(self):
        """ PUT запрос на обновление данных пользователя.
            Данные запроса передаются в json
            {"id_update":, "url":, "comment":, "user_id":}
            :param
                url - url ссылки.
                comment - комментарий к ссылке(описание).
                user_id - пользователь, кто добавил ссылку.
            :return Сообщение об успешности выполнения или ошибка.
        """
        try:
            data_json = request.get_json()
            # TODO обновлять может только тот пользователь что и добавил
            Database.update(data_response=data_json)

        except KeyError as e:
            return {'Error': f'Не задано <{e}>'}, 400
        except Exception as e:
            return {'Error': f'{e}'}, 400

        return {'message': f"Link update"}, 200


class ControllersLinkDelete(Resource):
    """ Удаляет ссылку из БД """
    def delete(self):
        """ DELETE запрос на удаление пользователя из БД.
            Данные запроса передаются в json {"id_delete":}
            :param
                id_delete - id пользователя в БД, которого надо удалить.
            :returns Сообщение об успешности выполнения или ошибка.
        """
        try:
            data_json = request.get_json()

            # TODO удалить может только тот пользователь что и добавил

            Database.dell(id_delete=data_json["id_delete"])

        except Exception as e:
            return {'Error': f'{e}'}, 400

        return {'message': f"Link delete"}, 200


class ControllersLinkGetAll(Resource):
    """ Возвращает все ссылки из БД """
    def get(self):
        """ GET запрос на получение списка всех пользователей в БД
            :return Список всех пользователей.
        """
        try:
            links = Link.query.all()

            all_link = dict()

            for link in links:
                all_link[link.id] = link.url

        except Exception as e:
            return {'Error': f'{e}'}, 400

        return all_link, 200


class ControllersUserLinksGet(Resource):
    """ Возвращает все ссылки пользователя """
    def get(self):
        """ GET запрос на получение данных о пользователе.
            Данные запроса передаются "?user_id="
            :param
                user_id - id пользователя.
            :return Сообщение об успешности выполнения или ошибка.
        """
        try:
            link_sh = LinkSchema(many=True)
            request_user_id = request.args.get('user_id')

            data_user = Link.query.filter(
                Link.user_id == request_user_id).all()

            data_user_sh = link_sh.dump(data_user)

        except Exception as e:
            return {'Error': f'{e}'}, 400

        return data_user_sh, 200


class ControllersTestWork(Resource):
    """ Проверка работоспособности сервиса """
    def get(self):
        """ GET запрос возвращает код 200. """
        return 200
