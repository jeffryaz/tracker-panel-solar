import asyncio
import time
import requests
import json
from threading import Thread
from flask import Flask, current_app


def say_after(delay, what):
    app = Flask(__name__)
    with app.app_context():
        time.sleep(delay)
        current_app.logger.debug(f' [IHG Provisioning] => payload {what}')


def call_me():
    Thread(target=say_after, args=(5, "Hallo")).start()

