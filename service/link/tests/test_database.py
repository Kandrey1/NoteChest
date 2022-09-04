from sqlalchemy import delete
from ..app.models import db, Link
from ..app.utils import Database


def test_db_link_1(app_test):
    """ Тестирование таблицы 'Link' """
    with app_test.app_context():
        link = Link(url='http://test.ru',
                    comment='test',
                    user_id=2)

        db.session.add(link)
        db.session.commit()

    assert Link.query.first().url == 'http://test.ru'
    assert Link.query.first().comment == 'test'
    assert Link.query.first().user_id == 2


def test_db_link_2(app_test):
    """ Тестирование таблицы 'Link' """
    with app_test.app_context():
        link1 = Link(url='http://test.ru',
                     comment='test',
                     user_id=2)

        link2 = Link(url='http://test1.ru',
                     comment='test1',
                     user_id=3)

        db.session.add(link1)
        db.session.add(link2)
        db.session.commit()

        assert Link.query.first().comment == 'test'

        db.session.execute(delete(Link).where(Link.id == 1))
        db.session.commit()

    assert Link.query.first().url == 'http://test1.ru'
    assert Link.query.first().comment == 'test1'
    assert Link.query.first().user_id == 3


def test_db_utils_db_save(app_test):
    """ Сохранение записи в БД """
    new_link = Link(url='http://test.ru',
                    comment='test',
                    user_id=2)

    Database.save(new_link)

    assert len(Link.query.all()) == 1
    assert Link.query.first().url == 'http://test.ru'
    assert Link.query.first().comment == 'test'


def test_db_utils_db_update(app_test):
    """ Обновление записи в БД """
    new_link = Link(url='http://test.ru',
                    comment='test',
                    user_id=2)
    up_link = {"id_update": 1,
               "url": "http://test1.ru",
               "comment": "test1",
               "user_id": 3}

    Database.save(new_link)
    assert len(Link.query.all()) == 1
    assert Link.query.first().url == 'http://test.ru'
    assert Link.query.first().comment == 'test'

    Database.update(up_link)
    assert len(Link.query.all()) == 1
    assert Link.query.first().url == 'http://test1.ru'
    assert Link.query.first().comment == 'test1'


def test_db_utils_db_dell(app_test):
    """ Удаление записи из БД """
    new_link1 = Link(url='http://test.ru',
                     comment='test',
                     user_id=2)

    new_link2 = Link(url='http://test1.ru',
                     comment='test1',
                     user_id=3)

    db.session.add(new_link1)
    db.session.add(new_link2)
    db.session.commit()

    assert len(Link.query.all()) == 2

    Database.dell(id_delete=1)
    assert len(Link.query.all()) == 1
    assert Link.query.first().url == 'http://test1.ru'
    assert Link.query.first().comment == 'test1'
