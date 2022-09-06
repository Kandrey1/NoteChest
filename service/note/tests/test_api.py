from ..app.models import db, Note


def test_controllers_note_add(client_test, app_test):
    data = {"text": "test text",
            "user_id": 2}

    response = client_test.post("/api/note/add", json=data)

    with app_test.app_context():
        note = Note.query.first()

    assert response.status_code == 200
    assert note.text == "test text"
    assert note.user_id == 2
    assert response.json == {'message': 'Note add'}


def test_controllers_note_update(client_test, app_test):
    data_update = {"id_update": 1,
                   "text": "test text1",
                   "user_id": 3}

    with app_test.app_context():
        note = Note(text="test text",
                    user_id=2)
        db.session.add(note)
        db.session.commit()

        assert Note.query.first().text == "test text"

    response = client_test.put("/api/note/update", json=data_update)

    assert response.status_code == 200
    assert response.json == {'message': 'Note update'}
    assert Note.query.first().text == "test text1"
    assert Note.query.first().user_id == 3


def test_controllers_note_delete(client_test, app_test):
    with app_test.app_context():
        note1 = Note(text="test text1",
                     user_id=2)

        note2 = Note(text="test text2",
                     user_id=3)

        db.session.add(note1)
        db.session.add(note2)
        db.session.commit()

        assert len(Note.query.all()) == 2
        assert Note.query.first().text == 'test text1'

        data_dell = {"id_delete": 1}

    response = client_test.delete("/api/note/delete", json=data_dell)

    assert response.status_code == 200
    assert len(Note.query.all()) == 1
    assert response.json == {'message': 'Note delete'}
    assert Note.query.first().text == "test text2"
    assert Note.query.first().user_id == 3


def test_controllers_note_get_all(client_test, app_test):
    with app_test.app_context():
        note1 = Note(text="test text1",
                     user_id=2)

        note2 = Note(text="test text2",
                     user_id=3)

        db.session.add(note1)
        db.session.add(note2)
        db.session.commit()

    response = client_test.get("/api/note/get_all")

    assert response.status_code == 200
    assert response.json == {'1': 'test text1', '2': 'test text2'}
    assert Note.query.first().text == "test text1"


def test_controllers_user_notes(client_test, app_test):
    with app_test.app_context():
        note1 = Note(text="test text1",
                     user_id=2)

        note2 = Note(text="test text2",
                     user_id=3)

        note3 = Note(text="test text3",
                     user_id=2)

        db.session.add(note1)
        db.session.add(note2)
        db.session.add(note3)
        db.session.commit()

    response = client_test.get("/api/note/get?user_id=2")

    assert response.status_code == 200
    assert len(response.json) == 2
    assert response.json[1]['text'] == 'test text3'
