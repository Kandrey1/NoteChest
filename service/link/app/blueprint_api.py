from flask import Blueprint
from flask_restful import Api
from .controllers import ControllersLinkAdd, ControllersLinkUpdate,\
    ControllersLinkDelete, ControllersLinkGetAll, ControllersUserLinksGet,\
    ControllersTestWork

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(ControllersLinkAdd, '/add')
api.add_resource(ControllersLinkUpdate, '/update')
api.add_resource(ControllersLinkDelete, '/delete')
api.add_resource(ControllersLinkGetAll, '/get_all')
api.add_resource(ControllersUserLinksGet, '/get')
# api для проверки работоспособности сервиса
api.add_resource(ControllersTestWork, '/test/work_service/status')
