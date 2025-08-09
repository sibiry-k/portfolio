from config.settings import config, testing_config
from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager

from .admin.views import MyAdminIndexView, ProjectView
from .db import db, init_db, migrate, wait_for_db


def create_app(flask_env=config.FLASK_ENV):
    app = Flask(__name__, instance_relative_config=True)
    login_manager = LoginManager()
    login_manager.init_app(app)

    if flask_env is None:
        flask_env = config.FLASK_ENV
    if flask_env == 'testing':
        app.config.from_object(testing_config)
    elif flask_env == 'development':
        app.config.from_object(config)
        app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')
        app.jinja_env.auto_reload = True
        app.config['DEBUG'] = True
    else:
        app.config.from_object(config)

    init_db(app)

    if flask_env != 'testing':
        with app.app_context():
            if not wait_for_db(app):
                print("Инициализация БД...")

    from . import views
    from .models import Project, User

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)

    if flask_env != 'testing':
        admin = Admin(
            app,
            name='Админка MyPortfolio',
            template_mode='bootstrap3',
            index_view=MyAdminIndexView(),
        )

        path = app.config['UPLOAD_FOLDER']

        admin.add_view(ModelView(User, db.session, name='Пользователи'))
        admin.add_view(ProjectView(Project, db.session, name='Проекты'))
        admin.add_view(FileAdmin(path, '/media_data/', name='Файлы'))

    app.register_blueprint(views.bp)

    return app
