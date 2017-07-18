#!/usr/bin/env python

from flask import abort, g, jsonify, abort, make_response
from flask_restful import Resource, reqparse, marshal_with, fields, marshal

from main.api import api

class NetworkApi(Resource):
    #decorators = [auth.login_required]

    def get(self):
        return jsonify({'network': 'hello'})

api.add_resource(NetworkApi, '/networks', endpoint = '/networks')


