import os


class Config:
    # app
    FLASK_APP = os.getenv('FLASK_APP')
    FLASK_ENV = os.getenv('FLASK_ENV')
    TEMPLATES_AUTO_RELOAD = True
    EXPLAIN_TEMPLATE_LOADING = True
    SECRET_KEY = os.getenv('SECRET_KEY')
    PROPAGATE_EXCEPTIONS = True
    # admin
    FLASK_ADMIN_SWATCH = 'cerulean'
    # db
    POSTGRES_DB = os.getenv("POSTGRES_DB", "")
    POSTGRES_USER = os.getenv("POSTGRES_USER", "")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT", 5432)
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@"
        f"{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    )
    # Images
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'media_data')
    ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']
    # YandexCloud
    CAPTCHA_CLIENT_KEY = os.getenv('CAPTCHA_CLIENT_KEY')
    CAPTCHA_SERVER_KEY = os.getenv('CAPTCHA_SERVER_KEY')


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql+psycopg2://{Config.POSTGRES_USER}:{Config.POSTGRES_PASSWORD}@"
        f"{Config.POSTGRES_HOST}:{Config.POSTGRES_PORT}/{Config.POSTGRES_DB}"
    )
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'test_media_data')


config = Config()
testing_config = TestingConfig()
