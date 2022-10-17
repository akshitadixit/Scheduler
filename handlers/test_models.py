import io
from click import FileError
from flask import Flask, url_for
import json

from routes import configure_routes
from models import main_func


def test_main_func__success():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    filepath = '../static/uploads/input1.txt'

    response = main_func()
    assert response.keys() == ['task id', 'task name', 'duration',
                               'ES', 'EF', 'LS', 'LF', 'float', 'isCritical']


def test_main_func__failure():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    filepath = '../static/uploads/test.jpg'

    with client.assertRaises(FileError) as context:
        main_func()
