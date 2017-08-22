# -*- coding: utf-8 -*-
"""
This is an example for a Flask WSGI application.

You can use it as a starting point for your application or delete the file.
"""

from json import dumps

from flask import Flask

flask_app = Flask(__name__)


@flask_app.route("/")
def sample_endpoint():
    """
    Sample endpoint returns Hello: World
    :return:
    """
    return dumps({"Hello": "World"}), 200
