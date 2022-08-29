from flask import Blueprint
from flask_restful import Api
from .controllers import ControllersUserRegister, ControllersUserAuth

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(ControllersUserRegister, '/user/register')
api.add_resource(ControllersUserAuth, '/user/auth')
