# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from flask import render_template, request
from jinja2 import TemplateNotFound


@blueprint.route('/')
def index():
    return render_template('home/index.html', segment='index')


@blueprint.route('/<template>')
def route_template(template):
    try:
        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template('home/index.html', segment='index')

    except TemplateNotFound:
        return render_template('home/index.html', segment='index')

    except:
        return render_template('home/index.html', segment='index')
