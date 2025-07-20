import time

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError

db = SQLAlchemy()
migrate = Migrate()


def init_db(app):
    db.init_app(app)
    migrate.init_app(app, db)


def wait_for_db(app):
    """Waits for db to become available"""
    with app.app_context():
        retries = 5
        while retries > 0:
            try:
                db.session.execute(db.text('SELECT 1'))
                print("DB is available")
                return True
            except OperationalError as e:
                print(f"OperationalError: {e}")
                time.sleep(5)
                retries -= 1
            except Exception as e:
                print(f"Exception: {e}")
                time.sleep(5)
                retries -= 1
        print("DB not available")
        return False
