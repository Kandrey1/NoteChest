from app import create_app
from config import Config
from app.models import db
from app.blueprint_api import api_bp
from flask_jwt_extended import JWTManager

app = create_app(Config)
jwt = JWTManager(app)


@app.before_first_request
def create_table():
    db.create_all()


app.register_blueprint(api_bp, url_prefix='/api')


@app.route("/")
def index():
    """ Представление главной страницы """
    context = dict()
    context['title'] = "Home"
    return {"Docker": "SERVICE USER"}


if __name__ == '__main__':
    app.run(host='0.0.0.0')
