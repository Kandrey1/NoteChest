class Config(object):
    DEBUG = True
    SECRET_KEY = '32498jkhsf123fdh123j213l2131f2jewf1fe21f1y3'

    JWT_SECRET_KEY = 'sdfhj;lh3423413sdfasdfa1345635'

    # Для локальной разработки и тестирования
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///db_user.sqlite'

    # Для образа Docker. Для работы с Postgres
    DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
        user='postgres', pw='pgpass', url='postgres:5432', db='note_chest')
    SQLALCHEMY_DATABASE_URI = DB_URL

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ConfigTest(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../tests/db_test.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'sdfhhghfg12321asdfa1345635'