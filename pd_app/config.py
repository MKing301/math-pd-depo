import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY_LOCAL')
    SQLALCHEMY_DATABASE_URI = os.environ.get('LOCAL_DB_URI_MATH')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
