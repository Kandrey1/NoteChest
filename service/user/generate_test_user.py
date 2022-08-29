from app import create_app
from config import Config
from app.models import db, User
app = create_app(Config)


def create_user():
    """ Создает пользователей в БД """

    user_name = ['admin', 'user1', 'user2', 'user3', 'user4', 'user5', 'user6',
                 'user7', 'user8', 'user9', 'user10']
    user_data = list()

    with app.app_context():
        for u in user_name:
            users = User(login=f'{u}', email=f'{u}@user',
                         password=f'pass_{u}')
            user_data.append(users)

        db.session.add_all(user_data)
        db.session.commit()


def set_data():
    create_user()


if __name__ == '__main__':
    set_data()
