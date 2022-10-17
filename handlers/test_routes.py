import io
from flask import Flask, url_for
import json

from routes import configure_routes


def test_base_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)
    assert response.status_code == 200


def test_scheduler_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/scheduler'

    response = client.get(url)
    assert response.status_code == 200


def test_input_route__success():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/input'

    mock_request_data = {
        'file': (io.BytesIO(b"random input text"), 'test_input.txt')
    }

    client.assertIn(b'Your item has been saved.', response.data)

    response = client.post(url, data=json.dumps(
        mock_request_data), follow_redirects=True,
        content_type='multipart/form-data')
    assert response.status_code == 200


def test_input_route__failure__bad_request():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/input'

    mock_request_data = {}

    client.assertIn(b'Your item has been saved.', response.data)

    response = client.post(url, data=json.dumps(
        mock_request_data), follow_redirects=True,
        content_type='multipart/form-data')
    assert response.status_code == 400


def test_form_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/form'

    mock_request_data = {
        'file': '../static/upload/test.jpg'
    }

    response = client.post(
        '/input',
        data=mock_request_data,
        follow_redirects=True
    )

    client.assertIn(b'File uploaded', response.data)
