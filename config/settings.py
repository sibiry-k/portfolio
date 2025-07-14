import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    # app
    FLASK_APP = os.getenv('FLASK_APP')
    TEMPLATES_AUTO_RELOAD = True
    EXPLAIN_TEMPLATE_LOADING = True
    SECRET_KEY = os.getenv('SECRET_KEY')
    # admin
    FLASK_ADMIN_SWATCH = 'cerulean'
    # db
    POSTGRES_NAME = os.getenv("POSTGRES_NAME", "")
    POSTGRES_USER = os.getenv("POSTGRES_USER", "")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT", 5432)

    @property
    def SQLALCHEMY_DATABASE_URI(cls):
        return (
            f"postgresql+psycopg2://{cls.POSTGRES_USER}:{cls.POSTGRES_PASSWORD}@"
            f"{cls.POSTGRES_HOST}:{cls.POSTGRES_PORT}/{cls.POSTGRES_NAME}"
        )


config = Config()
