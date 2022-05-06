

from flask_pymongo import PyMongo
from flask import abort


def setup_db(app):
    try:
        app.config['MONGO_URI'] = 'mongodb://localhost:27017/company'
        mongo = PyMongo(app)

        return mongo.db
    except Exception as ex:
        print('ERROR: Could not connect to Mongo')
        print('EXCEPTION', ex)

        abort(500)


