from config.settings import config
from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager

from .admin.views import MyAdminIndexView
from .db import db, init_db, migrate, wait_for_db


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    login_manager = LoginManager()
    login_manager.init_app(app)

    if test_config is None:
        app.config.from_object(config)
        app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')
        app.jinja_env.auto_reload = True
    else:
        app.config.from_mapping(test_config)

    init_db(app)

    with app.app_context():
        if not wait_for_db(app):
            print("Initializing database...")

    from . import views
    from .models import Project, User

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)

    admin = Admin(
        app,
        name='Админка MyPortfolio',
        template_mode='bootstrap3',
        index_view=MyAdminIndexView(),
    )

    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Project, db.session))

    app.register_blueprint(views.bp)

    return app
