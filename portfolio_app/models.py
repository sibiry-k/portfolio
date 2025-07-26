from datetime import UTC, datetime

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from .db import db


class User(UserMixin, db.Model):
    """Создание модели пользователя.

    id - уникальный номер записи
    created_at - дата и время создания записи
    username - имя пользователя
    email - адрес электронной почты
    password_hash - поле для хранения пароля в зашифрованном виде
    is_admin - признак наличия прав администратора
    img_path - поле для хранения пути к файлу изображения
    """

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now(UTC))
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    img_path = db.Column(db.String(120), nullable=True)

    def __repr__(self):
        return self.username

    def set_password(self, password):
        """Сохраняет пароль пользователя в виде hash-записи."""
        self.password_hash = generate_password_hash(password)
        return

    def check_password(self, password):
        """Устанавливает тождество введенного пароля с hash-записью в БД."""
        return check_password_hash(self.password_hash, password)


class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    role = db.Column(db.String(80), nullable=False)
    img_path = db.Column(db.String(120), nullable=False)
