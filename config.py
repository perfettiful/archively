import os

DB_NAME = os.environ.get("DB_NAME", "link_archive")
DB_USER = os.environ.get("DB_USER", "link_user")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "link_password")
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = os.environ.get("DB_PORT", "5432")

class Config:
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "super-secret-key")
