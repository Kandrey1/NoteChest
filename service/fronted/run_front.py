from flask import render_template
from flask_jwt_extended import JWTManager
from front_app import create_app
from front_app.blueprint_user import front_user_bp
from front_app.blueprint_link import front_link_bp
from front_app.blueprint_note import front_note_bp
from config import Config

app = create_app(Config)
jwt = JWTManager(app)

app.register_blueprint(front_user_bp, url_prefix='/user')
app.register_blueprint(front_link_bp, url_prefix='/link')
app.register_blueprint(front_note_bp, url_prefix='/note')


@app.route("/")
def index():
    """ Представление главной страницы """
    context = dict()
    context['title'] = "NoteChest"

    return render_template("index.html", context=context)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
