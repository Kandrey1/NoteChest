from flask import render_template
from front_app import create_app
from front_app.blueprint_user import front_user_bp
from config import Config

app = create_app(Config)


app.register_blueprint(front_user_bp, url_prefix='/user')


@app.route("/")
def index():
    """ Представление главной страницы """
    context = dict()
    context['title'] = "Home"
    return render_template("index.html", context=context)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
