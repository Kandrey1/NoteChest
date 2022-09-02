from flask import Flask


def create_app(config_class):
    app = Flask(__name__, static_folder="static")

    app.config.from_object(config_class)

    return app
