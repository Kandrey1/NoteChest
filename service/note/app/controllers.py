from flask import request
from flask_restful import Resource
from .utils import Database
from .models import Note, NoteSchema


class ControllersNoteAdd(Resource):
    """ Добавление заметки в БД """
    def post(self):
        """ POST запрос на добавление ссылки в БД.
            Данные запроса передаются в json
            {"text":, "user_id":}
            :param
                text - текст заметки.
                user_id - пользователь, который добавил заметку.
            :return
                Сообщение об успешности выполнения или ошибка.
        """
        try:
            data_json = request.get_json()

            if Note.query.filter(Note.text == data_json['text']).first():
                raise Exception("Такая заметка уже существует")

            new_note = Note(text=data_json['text'],
                            user_id=data_json['user_id'])

            Database.save(new_note)

        except Exception as e:
            return {'Error': f'{e}'}, 400

        return {'message': 'Note add'}, 200


class ControllersNoteUpdate(Resource):
    """ Обновляет данные заметки в БД """
    def put(self):
        """ PUT запрос на обновление данных пользователя.
            Данные запроса передаются в json
            {"id_update":, "text":, "user_id":}
            :param
                text - текст заметки.
                user_id - пользователь, который добавил заметку.
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

        return {'message': "Note update"}, 200


class ControllersNoteDelete(Resource):
    """ Удаляет заметку из БД """
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

        return {'message': "Note delete"}, 200


class ControllersNoteGetAll(Resource):
    """ Возвращает все ссылки из БД """
    def get(self):
        """ GET запрос на получение списка всех пользователей в БД
            :return Список всех пользователей.
        """
        try:
            notes = Note.query.all()

            all_note = dict()

            for note in notes:
                all_note[note.id] = note.text

        except Exception as e:
            return {'Error': f'{e}'}, 400

        return all_note, 200


class ControllersUserNotesGet(Resource):
    """ Возвращает все заметки пользователя """
    def get(self):
        """ GET запрос на получение данных о пользователе.
            Данные запроса передаются "?user_id="
            :param
                user_id - id пользователя.
            :return Сообщение об успешности выполнения или ошибка.
        """
        try:
            note_sh = NoteSchema(many=True)
            request_user_id = request.args.get('user_id')

            data_user = Note.query.filter(
                Note.user_id == request_user_id).all()

            data_user_sh = note_sh.dump(data_user)

        except Exception as e:
            return {'Error': f'{e}'}, 400

        return data_user_sh, 200


class ControllersTestWork(Resource):
    """ Проверка работоспособности сервиса """
    def get(self):
        """ GET запрос возвращает код 200. """
        return 200
