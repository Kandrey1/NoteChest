from sqlalchemy import delete
from ..app.models import db, Note
from ..app.utils import Database


def test_db_note_1(app_test):
    """ Тестирование таблицы 'Note' """
    with app_test.app_context():
        note = Note(text="test text1",
                    user_id=2)

        db.session.add(note)
        db.session.commit()

    assert Note.query.first().text == 'test text1'
    assert Note.query.first().user_id == 2


def test_db_note_2(app_test):
    """ Тестирование таблицы 'Note' """
    with app_test.app_context():
        note1 = Note(text="test text1",
                     user_id=2)

        note2 = Note(text="test text2",
                     user_id=3)

        db.session.add(note1)
        db.session.add(note2)
        db.session.commit()

        assert Note.query.first().text == 'test text1'

        db.session.execute(delete(Note).where(Note.id == 1))
        db.session.commit()

    assert Note.query.first().text == 'test text2'
    assert Note.query.first().user_id == 3


def test_db_utils_db_save(app_test):
    """ Сохранение записи в БД """
    new_note = Note(text="test text1",
                    user_id=2)

    Database.save(new_note)

    assert len(Note.query.all()) == 1
    assert Note.query.first().text == 'test text1'
    assert Note.query.first().user_id == 2


def test_db_utils_db_update(app_test):
    """ Обновление записи в БД """
    new_note = Note(text="test text1",
                    user_id=2)
    up_note = {"id_update": 1,
               "text": "test text2",
               "user_id": 3}

    Database.save(new_note)
    assert len(Note.query.all()) == 1
    assert Note.query.first().text == 'test text1'
    assert Note.query.first().user_id == 2

    Database.update(up_note)
    assert len(Note.query.all()) == 1
    assert Note.query.first().text == 'test text2'
    assert Note.query.first().user_id == 3


def test_db_utils_db_dell(app_test):
    """ Удаление записи из БД """
    new_note1 = Note(text="test text1",
                     user_id=2)

    new_note2 = Note(text="test text2",
                     user_id=3)

    db.session.add(new_note1)
    db.session.add(new_note2)
    db.session.commit()

    assert len(Note.query.all()) == 2

    Database.dell(id_delete=1)
    assert len(Note.query.all()) == 1
    assert Note.query.first().text == 'test text2'
    assert Note.query.first().user_id == 3
