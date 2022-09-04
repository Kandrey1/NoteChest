from ..app.models import db, Link


def test_controllers_link_add(client_test, app_test):
    data = {"url": "http://test.ru",
            "comment": "test",
            "user_id": 2}

    response = client_test.post("/api/link/add", json=data)

    with app_test.app_context():
        link = Link.query.first()

    assert response.status_code == 200
    assert link.url == "http://test.ru"
    assert link.comment == "test"
    assert link.user_id == 2
    assert response.json == {'message': 'Link add'}


def test_controllers_link_update(client_test, app_test):
    data_update = {"id_update": 1,
                   "url": "http://test1.ru",
                   "comment": "test1",
                   "user_id": 3}

    with app_test.app_context():
        link = Link(url="http://test.ru",
                    comment="test",
                    user_id=2)
        db.session.add(link)
        db.session.commit()

        assert Link.query.first().url == "http://test.ru"

    response = client_test.put("/api/link/update", json=data_update)

    assert response.status_code == 200
    assert response.json == {'message': 'Link update'}
    assert Link.query.first().url == "http://test1.ru"
    assert Link.query.first().comment == "test1"


def test_controllers_link_delete(client_test, app_test):
    with app_test.app_context():
        link1 = Link(url="http://test.ru",
                     comment="test",
                     user_id=2)

        link2 = Link(url="http://test1.ru",
                     comment="test1",
                     user_id=3)

        db.session.add(link1)
        db.session.add(link2)
        db.session.commit()

        assert len(Link.query.all()) == 2
        assert Link.query.first().url == 'http://test.ru'

        data_dell = {"id_delete": 1}

    response = client_test.delete("/api/link/delete", json=data_dell)

    assert response.status_code == 200
    assert len(Link.query.all()) == 1
    assert response.json == {'message': 'Link delete'}
    assert Link.query.first().url == "http://test1.ru"
    assert Link.query.first().comment == 'test1'


def test_controllers_link_get_all(client_test, app_test):
    with app_test.app_context():
        link1 = Link(url="http://test.ru",
                     comment="test",
                     user_id=2)

        link2 = Link(url="http://test1.ru",
                     comment="test1",
                     user_id=3)

        db.session.add(link1)
        db.session.add(link2)
        db.session.commit()

    response = client_test.get("/api/link/get_all")

    assert response.status_code == 200
    assert response.json == {'1': 'http://test.ru', '2': 'http://test1.ru'}
    assert Link.query.first().url == "http://test.ru"


def test_controllers_user_links(client_test, app_test):
    with app_test.app_context():
        link1 = Link(url="http://test.ru",
                     comment="test",
                     user_id=2)

        link2 = Link(url="http://test1.ru",
                     comment="test",
                     user_id=3)

        link3 = Link(url="http://test2.ru",
                     comment="test",
                     user_id=2)

        db.session.add(link1)
        db.session.add(link2)
        db.session.add(link3)
        db.session.commit()

    response = client_test.get("/api/link/get?user_id=2")

    assert response.status_code == 200
    assert len(response.json) == 2
    assert response.json[1]['url'] == 'http://test2.ru'
