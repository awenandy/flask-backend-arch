#!/usr/bin/env python

from flask import Blueprint
from flask.ext.restful import Api, Resource, reqparse, fields, marshal

api_blueprint = Blueprint("api", __name__, url_prefix='/api')
api = Api(api_blueprint)

from . import host
from . import network

