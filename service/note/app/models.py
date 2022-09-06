import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

ma = Marshmallow()
db = SQLAlchemy()


class Note(db.Model):
    """ Таблица заметок """
    __tablename__ = 'note'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400), nullable=False)
    create = db.Column(db.DateTime, default=datetime.datetime.today())
    user_id = db.Column(db.Integer, nullable=False)

    def __init__(self, text, user_id):
        self.text = text
        self.user_id = user_id

    def __repr__(self):
        return f"<User id={self.user_id} - {self.text}>"


class NoteSchema(ma.Schema):
    class Meta:
        model = Note
        fields = ('id', 'text', 'create', 'user_id')
