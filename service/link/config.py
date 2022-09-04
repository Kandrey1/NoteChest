class Config(object):
    DEBUG = True
    SECRET_KEY = '32498jkhsf123fdh123j213l2131f2jewf1fe21f1y3'

    # Для локальной разработки и тестирования
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///db_link.sqlite'

    # Для образа Docker. Для работы с Postgres
    DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
        user='postgres', pw='pgpass', url='postgres:5432', db='user')
    SQLALCHEMY_DATABASE_URI = DB_URL

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ConfigTest(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../tests/db_test.sqlite'
