#!/usr/bin/env python

import os
from flask import Flask
from main.settings import ProdConfig, DevConfig
from main.api import api_blueprint

app = Flask(__name__)

if os.getenv("FLASK_ENV") == 'prod':
    DefaultConfig = ProdConfig
else:
    DefaultConfig = DevConfig

def init_app(db,config_object=DefaultConfig):
    app.config.from_object(config_object)
    register_extensions(app,db)
    register_blueprints(app)

    return app

def register_extensions(app,db):
    #db.init_app(app)
    db.create_all()
    #migrate.init_app(app, db)
    pass

def register_blueprints(app):
    app.register_blueprint(api_blueprint)


