class Config(object):
    DEBUG = True
    SECRET_KEY = '32498jkhsf123fdh123j213l2131f2jewf1fe21f1y3'

    JWT_SECRET_KEY = 'sdfhj;lh3423413sdfasdfa1345635'

    DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
        user="postgres", pw="pgpass", url="postgres:5432", db="user_db")

    SQLALCHEMY_DATABASE_URI = DB_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
