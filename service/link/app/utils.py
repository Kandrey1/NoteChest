from sqlalchemy import update, delete
from .models import db, Link


class Database:
    """ Методы для работы с БД """
    @classmethod
    def save(cls, new_link: object) -> None:
        """ Сохраняет запись в БД. При неудаче возвращает ошибку.
            :param
                new_link - экземпляр класса Link таблицы в БД
        """
        try:
            db.session.add(new_link)
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            raise Exception(f"Ошибка при сохранении в БД: <{e}>")

    @classmethod
    def update(cls, data_response: dict) -> None:
        """ Обновляет данные записи в БД.
            :param
                data_response - json данные в запросе
                                {"id_update": , "url": , "comment": ,
                                 "user_id": }
        """
        try:
            data_update = {"url": data_response['url'],
                           "comment": data_response['comment'],
                           "user_id": data_response['user_id']}

            if data_response['id_update']:
                db.session.execute(update(Link).
                                   where(Link.id == data_response['id_update']).
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
            db.session.execute(delete(Link).where(Link.id == id_delete))
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            raise Exception(f"Ошибка при удалении записи из БД: <{e}>")
