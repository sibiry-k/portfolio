from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    url_for,
)
from flask_login import login_required, login_user, logout_user

from .db import db
from .forms import LoginForm, RegistrationForm
from .models import User

bp = Blueprint('main', __name__)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if User.query.filter_by(username=form.username.data).first():
            flash('Пользователь с таким именем уже существует')
            return redirect(url_for('main.register'))

        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('main.login'))
    return render_template('base/register.pug', form=form)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login_user(form.get_user())

        flash('Вы успешно вошли')

        return redirect(url_for('admin.index'))
    return render_template('base/login.pug', form=form)


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@bp.route('/')
def index():
    return render_template("index.pug")
