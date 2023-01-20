# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os


class Config(object):

    basedir = os.path.abspath(os.path.dirname(__file__))

    # Set up the App SECRET_KEY
    # SECRET_KEY = config('SECRET_KEY'  , default='S#perS3crEt_007')
    SECRET_KEY = os.getenv('SECRET_KEY', 'S#perS3crEt_007')
    OCA_URL = os.getenv(
        'OCA_URL', 'https://email.ocatelkom.co.id/api/v1/send-single')
    OCA_UNAME = os.getenv('OCA_UNAME', 'dradjat@melon.co.id')
    OCA_PASSWORD = os.getenv('OCA_PWD', 'ocatelkom')
    OCA_SENDER_EMAIL = os.getenv(
        'OCA_SENDER_EMAIL', 'noreply@indihomegamer.id')

    # This will create a file in <app> FOLDER
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
    #     os.path.join(basedir, 'db.sqlite3')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Assets Management
    ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets')
    ASSETS_PATH = os.path.dirname(os.path.abspath(
        __file__ + "../../" + ASSETS_ROOT + '/assets'))
    ATLAS_URI = 'mongodb://localhost:27017/?readPreference=primary&ssl=false&directConnection=true&replicaSet=rs0'
    DB_NAME = 'testing-local'


class ProductionConfig(Config):
    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    # PostgreSQL database
    # SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
    #     os.getenv('DB_ENGINE', 'mysql'),
    #     os.getenv('DB_USERNAME', 'appseed_db_usr'),
    #     os.getenv('DB_PASS', 'pass'),
    #     os.getenv('DB_HOST', 'localhost'),
    #     os.getenv('DB_PORT', 3306),
    #     os.getenv('DB_NAME', 'appseed_db')
    # )


class DebugConfig(Config):
    DEBUG = True


# Load all possible configurations
config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig
}
