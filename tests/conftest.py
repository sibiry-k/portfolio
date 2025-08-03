import os
import shutil
import sys
import tempfile

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from portfolio_app import create_app
from portfolio_app.db import db
from portfolio_app.models import Project, User


@pytest.fixture(scope='session')
def app():
    """Создает Flask app для тестов."""
    test_media_dir = tempfile.mkdtemp()

    app = create_app('testing')
    app.config['UPLOAD_FOLDER'] = test_media_dir
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False

    with app.app_context():
        db.create_all()

        yield app

        db.session.remove()
        db.drop_all()
        shutil.rmtree(test_media_dir, ignore_errors=True)


@pytest.fixture
def client(app):
    """Предоставляет тестовый клиент для отправки запросов."""
    return app.test_client()


@pytest.fixture
def runner(app):
    """Предоставляет runner для CLI команд."""
    return app.test_cli_runner()


@pytest.fixture(autouse=True)
def clean_db(app):
    """Очищает БД перед каждым тестом."""
    with app.app_context():
        for table in reversed(db.metadata.sorted_tables):
            db.session.execute(table.delete())
        db.session.commit()

    yield

    with app.app_context():
        db.session.rollback()


@pytest.fixture
def test_user(app):
    """Создает тестового пользователя."""
    with app.app_context():
        user = User(
            username="testuser",
            email="test@example.com",
        )
        user.set_password('testpassword')
        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)
        return user


@pytest.fixture
def test_project(app, test_user):
    """Создает тестовый проект."""
    with app.app_context():
        project = Project(
            title="Test Project",
            description="Test description",
            user_id=test_user.id,
        )
        db.session.add(project)
        db.session.commit()
        db.session.refresh(project)
        return project
