from flask import Flask, render_template
from flask_admin import Admin
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from settings import config

app = Flask(__name__)
app.config.from_object(config)

admin = Admin(app, name='portfolio', template_mode='bootstrap3')

app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)


@app.route('/')
def index():
    return render_template('index.pug')


if __name__ == '__main__':
    app.run()
