from flask import Blueprint
from flask_restful import Api
from .controllers import ControllersUserRegister, ControllersUserAuth, \
    ControllersUserCrud, ControllersUserLogout, ControllersUserGetAll, \
    ControllersUserGet, ControllersTestWork

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(ControllersUserRegister, '/register')
api.add_resource(ControllersUserAuth, '/auth')
api.add_resource(ControllersUserLogout, '/logout')
api.add_resource(ControllersUserCrud, '/crud')
api.add_resource(ControllersUserGetAll, '/get_all')
api.add_resource(ControllersUserGet, '/get')
# api для проверки работоспособности сервиса
api.add_resource(ControllersTestWork, '/test/work_service/status')
