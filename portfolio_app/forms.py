from flask_wtf import FlaskForm
from werkzeug.security import check_password_hash
from wtforms.fields.simple import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError

from .db import db
from .models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('<PASSWORD>', validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

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
