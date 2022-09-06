from flask import Blueprint
from flask_restful import Api
from .controllers import ControllersNoteAdd, ControllersNoteUpdate,\
    ControllersNoteDelete, ControllersNoteGetAll, ControllersUserNotesGet,\
    ControllersTestWork

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(ControllersNoteAdd, '/add')
api.add_resource(ControllersNoteUpdate, '/update')
api.add_resource(ControllersNoteDelete, '/delete')
api.add_resource(ControllersNoteGetAll, '/get_all')
api.add_resource(ControllersUserNotesGet, '/get')
# api для проверки работоспособности сервиса
api.add_resource(ControllersTestWork, '/test/work_service/status')
