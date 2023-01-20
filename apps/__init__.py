import os
from flask import Flask
from importlib import import_module
from pymongo import MongoClient
from apps.config import config_dict
from apps.database import Database

DEBUG = (os.getenv('DEBUG', 'False') == 'True')

get_config_mode = 'Debug' if DEBUG else 'Production'

try:
    app_config = config_dict[get_config_mode.capitalize()]

except KeyError:
    exit('Error: Invalid <config_mode>. Expected values [Debug, Production] ')


def register_extensions(app):
    app.database = Database()


def register_blueprints(app):

    for module_name in ['home', 'api']:
        module = import_module('apps.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)


def create_app(config):

    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    return app
