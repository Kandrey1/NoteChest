from ..app.models import db, User


def test_controllers_user_register(client_test, app_test):
    data = {"login": "user1",
            "email": "user1@user",
            "password": "password_user1"}

    response = client_test.post("/api/user/register", json=data)

    with app_test.app_context():
        user = User.query.first()

    assert response.status_code == 200
    assert user.email == "user1@user"
    assert user.login == "user1"
    assert response.json['access_token']


def test_controllers_user_auth(client_test, app_test):
    with app_test.app_context():
        user1 = User(login='user1',
                     email='user1@user',
                     password="password_user1")

        db.session.add(user1)
        db.session.commit()

        assert len(User.query.all()) == 1
        assert User.query.first().login == 'user1'

    data = {"email": "user1@user",
            "password": "password_user1"}

    response = client_test.post("/api/user/auth", json=data)

    assert response.status_code == 200
    assert response.json['access_token']


def test_controllers_user_update(client_test, app_test):
    data_update = {"id_update": 1,
                   "login": "user2",
                   "email": "user2@user",
                   "password": "password_user2"}

    with app_test.app_context():
        user = User(login="user1", email="user1@user",
                    password="password_user1")
        db.session.add(user)
        db.session.commit()

        assert User.query.first().email == "user1@user"

    response = client_test.put("/api/user/crud", json=data_update)

    assert response.status_code == 200
    assert response.json == {'message': 'Data user id=1 update'}
    assert User.query.first().email == "user2@user"


def test_controllers_user_dell(client_test, app_test):
    with app_test.app_context():
        user1 = User(login='user1',
                     email='user1@user',
                     password="password_user1")

        user2 = User(login='user2',
                     email='user2@user',
                     password="password_user2")

        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()

        assert len(User.query.all()) == 2
        assert User.query.first().login == 'user1'

        data_dell = {"id_delete": 1}

    response = client_test.delete("/api/user/crud", json=data_dell)

    assert response.status_code == 200
    assert len(User.query.all()) == 1
    assert response.json == {'message': 'User id=1 delete'}
    assert User.query.first().email == "user2@user"
    assert User.query.first().login == 'user2'


def test_controllers_user_get_all(client_test, app_test):
    with app_test.app_context():
        user1 = User(login='user1',
                     email='user1@user',
                     password="password_user1")

        user2 = User(login='user2',
                     email='user2@user',
                     password="password_user2")

        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()

    response = client_test.get("/api/user/get_all")

    assert response.status_code == 200
    assert response.json == {'1': 'user1', '2': 'user2'}
    assert User.query.first().email == "user1@user"
    assert User.query.first().login == 'user1'


def test_controllers_user_get_data_one(client_test, app_test):
    with app_test.app_context():
        user1 = User(login='user1',
                     email='user1@user',
                     password="password_user1")

        user2 = User(login='user2',
                     email='user2@user',
                     password="password_user2")

        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()

    response = client_test.get("/api/user/get?user_id=2")

    assert response.status_code == 200
    assert response.json['email'] == 'user2@user'
    assert response.json['login'] == 'user2'
