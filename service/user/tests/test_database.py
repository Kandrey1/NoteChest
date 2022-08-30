from sqlalchemy import delete
from passlib.hash import bcrypt
from ..app.models import db, User
from ..app.utils import Database


def test_db_user_1(app_test):
    """ Тестирование таблицы 'User' """
    with app_test.app_context():
        user = User(login='user1',
                    email='user1@user',
                    password='pass_user1')

        db.session.add(user)
        db.session.commit()

    assert User.query.first().login == 'user1'
    assert User.query.first().email == 'user1@user'
    assert bcrypt.verify('pass_user1', User.query.first().password)


def test_db_user_2(app_test):
    """ Тестирование таблицы 'User' """
    with app_test.app_context():
        user1 = User(login='user1',
                     email='user1@user',
                     password='password_user1')

        user2 = User(login='user2',
                     email='user2@user',
                     password='password_user2')

        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()

        assert User.query.first().login == 'user1'

        db.session.execute(delete(User).where(User.id == 1))
        db.session.commit()

    assert User.query.first().login == 'user2'
    assert User.query.first().email == 'user2@user'
    assert bcrypt.verify('password_user2', User.query.first().password)


def test_db_utils_db_save(app_test):
    """ Сохранение записи в БД """
    new_user = User(login='user1',
                    email='user1@user',
                    password='password_user1')

    Database.save(new_user)

    assert len(User.query.all()) == 1
    assert User.query.first().login == 'user1'
    assert User.query.first().email == 'user1@user'
    assert bcrypt.verify('password_user1', User.query.first().password)


def test_db_utils_db_update(app_test):
    """ Обновление записи в БД """
    new_user = User(login='user1',
                    email='user1@user',
                    password='password_user1')
    up_user = {"id_update": 1,
               "login": "user2",
               "email": "user2@user",
               "password": "password_user2"}

    Database.save(new_user)
    assert len(User.query.all()) == 1
    assert User.query.first().login == 'user1'
    assert User.query.first().email == 'user1@user'
    assert bcrypt.verify('password_user1', User.query.first().password)

    Database.update(up_user)
    assert len(User.query.all()) == 1
    assert User.query.first().login == 'user2'
    assert User.query.first().email == 'user2@user'
    assert bcrypt.verify('password_user2', User.query.first().password)


def test_db_utils_db_dell(app_test):
    """ Удаление записи из БД """
    new_user1 = User(login='user1',
                     email='user1@user',
                     password='password_user1')

    new_user2 = User(login='user2',
                     email='user2@user',
                     password='password_user2')

    db.session.add(new_user1)
    db.session.add(new_user2)
    db.session.commit()

    assert len(User.query.all()) == 2

    Database.dell(id_delete=1)
    assert len(User.query.all()) == 1
    assert User.query.first().login == 'user2'
    assert User.query.first().email == 'user2@user'
    assert bcrypt.verify('password_user2', User.query.first().password)
