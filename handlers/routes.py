from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
from models import main_func


def configure_routes(app):

    @app.route("/", methods=['GET', 'POST'])
    def start():
        return render_template("index.html")

    @app.route("/scheduler", methods=['GET', 'POST'])
    def scheduling_table():
        return render_template("table.html")

    @app.route("/form", methods=['GET', 'POST'])
    def input_page():
        return render_template("input.html")

    @app.route("/input", methods=['POST'])
    def take_input():
        f = request.files['grammar']
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'static/uploads',
                                 secure_filename(f.filename))
        f.save(file_path)
        print(file_path)
        data = main_func(file_path)
        return render_template("table.html", data=data)
