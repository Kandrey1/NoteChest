import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

ma = Marshmallow()
db = SQLAlchemy()


class Link(db.Model):
    """ Таблица ссылок """
    __tablename__ = 'link'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(250), nullable=False)
    comment = db.Column(db.String(250), nullable=False)
    create = db.Column(db.DateTime, default=datetime.datetime.today())
    user_id = db.Column(db.Integer, nullable=False)

    def __init__(self, url, comment, user_id):
        self.url = url
        self.comment = comment
        self.user_id = user_id

    def __repr__(self):
        return f"<User id={self.user_id} - {self.url} - {self.comment}>"


class LinkSchema(ma.Schema):
    class Meta:
        model = Link
        fields = ('id', 'url', 'comment', 'create', 'user_id')
