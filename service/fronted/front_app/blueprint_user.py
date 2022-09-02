import requests
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .api_services.user import *

front_user_bp = Blueprint('fronted_user', __name__)


@front_user_bp.route("/register", methods=['GET', 'POST'])
def register():
    """ Представления для страницы регистрации нового пользователя """
    context = dict()
    context['title'] = 'Регистрация'
    try:
        if request.method == "POST":
            data_new_user = {"login": request.form.get('name'),
                             "email": request.form.get('email'),
                             "password": request.form.get('password')}

            url = f'{SERVICE_USER_HOST}{SERVICE_USER_REGISTER}'

            response = requests.post(url, json=data_new_user)

            if response.status_code == 400:
                raise Exception(f"{response.json()['Error']}")

            if response.status_code not in [200, 400]:
                raise Exception(f"{response.status_code } - Неизвестная ошибка")

            return redirect(url_for('fronted_user.profile'))

    except Exception as e:
        flash(f'Error. <{e}>')

    return render_template("user/register.html", context=context)


@front_user_bp.route("/auth", methods=['GET', 'POST'])
def auth():
    """ Представления для страницы авторизации """
    context = dict()
    context['title'] = 'Авторизация'
    try:
        if request.method == "POST":
            data_auth_user = {"email": request.form.get('email'),
                              "password": request.form.get('password')}

            url = f'{SERVICE_USER_HOST}{SERVICE_USER_AUTH}'

            response = requests.post(url, json=data_auth_user, timeout=5)

            if response.status_code == 400:
                raise Exception(f"{response.json()['Error']}")

            if response.status_code not in [200, 400]:
                raise Exception(f"{response.status_code } - Неизвестная ошибка")

            return redirect(url_for('fronted_user.profile'))

    except Exception as e:
        flash(f'{e}')

    return render_template("user/auth.html", context=context)


@front_user_bp.route("/logout", methods=['GET', 'POST'])
def logout():
    """ Представления для logout """
    return "logout"


@front_user_bp.route("/profile", methods=['GET', 'POST'])
def profile():
    """ Представления для личного кабинете """
    context = dict()
    context['title'] = 'Личный кабинет'
    return render_template("user/profile.html", context=context)


@front_user_bp.route("/test/work_service/status", methods=['GET'])
def test_service():
    """ Представления для проверки статуса сервиса """
    return {"status": "OK"}
