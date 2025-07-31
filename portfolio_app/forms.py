import logging

import requests
from flask import current_app
from flask_wtf import FlaskForm
from werkzeug.security import check_password_hash
from wtforms.fields.simple import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError

from .db import db
from .models import User

logger = logging.getLogger(__name__)


class YandexCaptchaMixin:
    """Миксин для добавления капчи к формам."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.captcha_server_key = current_app.config.get('CAPTCHA_SERVER_KEY')

    def validate_captcha(self, token, ip_address):
        if not token:
            logger.warning('Токен капчи отсутствует.')
            return False, 'Подтвердите, что вы не робот, пройдите капчу'
        if not self.captcha_server_key:
            logger.warning('Серверный ключ капчи не настроен.')
            return False, 'Серверный ключ капчи не настроен.'

        try:
            response = requests.post(
                'https://smartcaptcha.yandexcloud.net/validate',
                data={
                    'secret': self.captcha_server_key,
                    'token': token,
                    'ip': ip_address,
                },
                timeout=10,
            )
            response.raise_for_status()
            result = response.json()

            if result.get('status') == 'ok':
                return True, 'Капча пройдена'

            if not result.get('status') == 'ok':
                return 'Ошибка: капча не пройдена', 400
        except requests.exceptions.RequestException as e:
            logger.warning(f'Ошибка соединения с сервисом капчи: {e}')
            return False, f'Ошибка соединения с сервисом капчи: {e}'
        except ValueError as e:
            logger.warning(f'Ошибка обработки ответа капчи: {e}')
            return False, f'Ошибка обработки ответа капчи: {e}'

    def get_captcha_client_key(self):
        return current_app.config.get('CAPTCHA_CLIENT_KEY')


class RegistrationForm(FlaskForm):
    """Форма регистрации."""

    username = StringField('Имя пользователя', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Введите пароль', validators=[DataRequired()])
    password2 = PasswordField('Повторите пароль', validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')


class CaptchaRegistrationForm(YandexCaptchaMixin, RegistrationForm):
    """Форма регистрации с капчей."""

    pass


class LoginForm(FlaskForm):
    """Форма авторизации."""

    username = StringField('Имя пользователя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')

    def validate_username(self, username):
        user = self.get_user()

        if user is None:
            raise ValidationError('Такого пользователя не существует')
        if not check_password_hash(user.password_hash, self.password.data):
            raise ValidationError('неверный пароль')

    def get_user(self):
        return (
            db.session.query(User)
            .filter_by(username=self.username.data)
            .first()
        )
