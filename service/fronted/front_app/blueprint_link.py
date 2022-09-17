import requests
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_jwt_extended import jwt_required, get_jwt_identity
from .api_services.link import SERVICE_LINK_HOST, SERVICE_LINK_GET, \
    SERVICE_LINK_ADD, SERVICE_LINK_DELETE


front_link_bp = Blueprint('fronted_link', __name__)


@front_link_bp.route("/user", methods=['GET', 'POST'])
@jwt_required()
def links():
    """ Представление для ccылок """
    context = dict()
    try:
        current_user = get_jwt_identity()
        context['current_user'] = current_user
        context['title'] = 'Полезные ссылки'

        url_get = f'{SERVICE_LINK_HOST}{SERVICE_LINK_GET}?user_id=' \
                  f'{current_user}'
        context['links'] = requests.get(url_get).json()

        if request.method == "POST":
            if "link_add" in request.form:
                url_add = f'{SERVICE_LINK_HOST}{SERVICE_LINK_ADD}'

                data_link = {"url": request.form.get('link'),
                             "comment": request.form.get('link__comment'),
                             "user_id": current_user}

                response = requests.post(url_add, json=data_link)

                if response.status_code == 400:
                    raise Exception(f"{response.json()['Error']}")

                if response.status_code not in [200, 400]:
                    raise Exception(f"{response.status_code } "
                                    f"- Неизвестная ошибка")

                return redirect(url_for('fronted_link.links'))

            if "del_link" in request.form:
                url_del = f'{SERVICE_LINK_HOST}{SERVICE_LINK_DELETE}'

                data_link = {"id_delete": request.form.get('del_link')}

                response = requests.delete(url_del, json=data_link)

                if response.status_code == 400:
                    raise Exception(f"{response.json()['Error']}")

                if response.status_code not in [200, 400]:
                    raise Exception(f"{response.status_code } "
                                    f"- Неизвестная ошибка")

                return redirect(url_for('fronted_link.links'))

    except Exception as e:
        flash(f'Error. <{e}>')

    return render_template("link/links_user.html", context=context)
