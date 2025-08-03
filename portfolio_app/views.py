from config.settings import config
from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
)
from flask_login import current_user, login_required, login_user, logout_user

from .db import db
from .forms import CaptchaRegistrationForm, LoginForm
from .models import Project, User

bp = Blueprint('main', __name__)


@bp.route('/media_data/<path:filename>')
def media_data_files(filename):
    """Отдает маршрут к папке загрузки."""
    return send_from_directory(config.UPLOAD_FOLDER, filename)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    """Регистрирует пользователя."""

    form = CaptchaRegistrationForm()
    if form.validate_on_submit():
        token = request.form.get('smart-token')

        is_valid, error_message = form.validate_captcha(
            token, request.remote_addr
        )

        if not is_valid:
            flash(error_message)
            return render_template(
                'base/register.pug',
                form=form,
                captcha_key=form.get_captcha_client_key(),
            )

        if User.query.filter_by(username=form.username.data).first():
            flash('Пользователь с таким именем уже существует')
            return redirect(url_for('main.register'))

        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        if User.query.count() == 0:
            user.is_admin = True
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('main.login'))
    return render_template(
        'base/register.pug',
        form=form,
        captcha_key=form.get_captcha_client_key(),
    )


@bp.route('/login', methods=['GET', 'POST'])
def login():
    """Авторизует текущего пользователя."""
    form = LoginForm()
    if form.validate_on_submit():
        login_user(form.get_user())
        flash('Вы успешно вошли')
        return redirect(url_for('admin.index'))
    return render_template('base/login.pug', form=form)


@bp.route('/logout')
@login_required
def logout():
    """Снимает авторизацию текущему пользователю."""
    logout_user()
    return redirect(url_for('main.index'))


@bp.route('/lk')
@login_required
def lk():
    """Отображает личный кабинет пользователя."""
    user = User.query.filter_by(username=current_user.username).first()
    return render_template('lk.pug', user=user)


@bp.route('/')
def index():
    """Отображает главную страницу."""
    projects = Project.query.all()
    return render_template('index.pug', projects=projects)


@bp.route('/error500')
def get_error_500():
    """Выдает сообщение об ошибке 500."""
    error500 = 1 / 0
    return error500
