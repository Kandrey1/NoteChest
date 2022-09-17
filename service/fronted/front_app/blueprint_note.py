import requests
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_jwt_extended import jwt_required, get_jwt_identity
from .api_services.note import SERVICE_NOTE_HOST, SERVICE_NOTE_ADD, \
    SERVICE_NOTE_DELETE, SERVICE_NOTE_GET


front_note_bp = Blueprint('fronted_note', __name__)


@front_note_bp.route("/user", methods=['GET', 'POST'])
@jwt_required()
def notes():
    """ Представление для заметок """
    context = dict()
    try:
        current_user = get_jwt_identity()
        context['current_user'] = current_user
        context['title'] = 'Заметки'

        url_get = f'{SERVICE_NOTE_HOST}{SERVICE_NOTE_GET}?user_id=' \
                  f'{current_user}'
        context['notes'] = requests.get(url_get).json()

        if request.method == "POST":
            if "note_add" in request.form:
                url_add = f'{SERVICE_NOTE_HOST}{SERVICE_NOTE_ADD}'

                data_note = {"text": request.form.get('note'),
                             "user_id": current_user}

                response = requests.post(url_add, json=data_note)

                if response.status_code == 400:
                    raise Exception(f"{response.json()['Error']}")

                if response.status_code not in [200, 400]:
                    raise Exception(f"{response.status_code } "
                                    f"- Неизвестная ошибка")

                return redirect(url_for('fronted_note.notes'))

            if "del_note" in request.form:
                url_del = f'{SERVICE_NOTE_HOST}{SERVICE_NOTE_DELETE}'

                data_note = {"id_delete": request.form.get('del_note')}

                response = requests.delete(url_del, json=data_note)

                if response.status_code == 400:
                    raise Exception(f"{response.json()['Error']}")

                if response.status_code not in [200, 400]:
                    raise Exception(f"{response.status_code } "
                                    f"- Неизвестная ошибка")

                return redirect(url_for('fronted_note.notes'))

    except Exception as e:
        flash(f'Error. <{e}>')

    return render_template("note/notes_user.html", context=context)
