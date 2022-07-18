import os

from flask import Flask, flash, jsonify, render_template, abort, request
from flask_cors import CORS

from backend.database.model import setup_db


def create_app(test_config=None):
    # create and configure the app
    template_dir = os.path.abspath('frontend/templates')
    app = Flask(__name__, template_folder=template_dir)
    app.config['EXPLAIN_TEMPLATE_LOADING'] = True
    app.config['SECRET_KEY'] = 'supposed_to_be_secret'
    db = setup_db(app)

    CORS(app, resources={r"*": {"origins": "*"}})

    @app.after_request
    def after_request(res):
        res.headers.add("Access-Control-Allow-Headers",
                        "Content-Type, authorization, true")

        res.headers.add("Access-Control-Allow-Methods",
                        'GET, POST, PATCH, DELETE, OPTIONS')

        return res

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/users')
    def user_form():
        try:
            return render_template('forms/create_user.html')
        except Exception as ex:
            print('EXCEPTION', ex)
            abort(404)
    @app.route('/30-day-challenge')
    def challenge_30():
        return render_template('pages/30_day_challenge.html')

    @app.route('/60-day-challenge')
    def challenge_60():
        return render_template('pages/60_day_challenge.html')

    @app.route('/90-day-challenge')
    def challenge_90():
        return render_template('90_day_challenge.html')

    return app
