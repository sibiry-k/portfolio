from flask import Flask
from flask_admin import Admin

from . import views


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_pyfile('settings.py', silent=True)
        app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')
        app.jinja_env.auto_reload = True
    else:
        app.config.from_mapping(test_config)

    app.register_blueprint(views.bp)

    admin = Admin(app, name='MyPortfolio', template_mode='bootstrap3')  # noqa: F841

    return app
