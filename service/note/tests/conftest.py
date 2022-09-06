import pytest
from ..config import ConfigTest
from ..app import create_app
from ..app.models import db


@pytest.fixture
def app_test():
    app = create_app(config_class=ConfigTest)

    with app.app_context():
        db.create_all()

        yield app

        db.drop_all()


@pytest.fixture
def client_test(app_test):
    from ..app.blueprint_api import api_bp
    app_test.register_blueprint(api_bp, url_prefix='/api/note')

    return app_test.test_client()
