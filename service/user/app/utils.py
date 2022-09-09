from sqlalchemy import update, delete
from .models import db, User


class Database:
    """ Методы для работы с БД """
    @classmethod
    def save(cls, new_user: object) -> None:
        """ Сохраняет запись в БД. При неудаче возвращает ошибку.
            :param
                new_user - экземпляр класса User таблицы в БД
        """
        try:
            db.session.add(new_user)
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            raise Exception(f"Ошибка при сохранении в БД: <{e}>")

    @classmethod
    def update(cls, data_response: dict) -> None:
        """ Обновляет данные записи в БД.
            :param
                data_response - json данные в запросе
                                {"id_update": , "login": , "email": ,
                                 "password": }
        """
        try:
            data_update = {"login": data_response['login'],
                           "email": data_response['email'],
                           "password": User.get_hash_pass(
                                data_response['password'])}

            if data_response['id_update']:
                db.session.execute(update(User).
                                   where(User.id == data_response['id_update']).
                                   values(data_update))
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            raise Exception(f"Ошибка при обновлении записи в БД: <{e}>")

    @classmethod
    def dell(cls, id_delete: int) -> None:
        """ Удаляет запись из БД.
            :param
                id_delete - id записи, которую требуется удалить.
        """
        try:
            db.session.execute(delete(User).where(User.id == id_delete))
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            raise Exception(f"Ошибка при удалении записи из БД: <{e}>")
