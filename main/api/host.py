#!/usr/bin/env python

from flask import abort, g, jsonify, abort, make_response
from flask_restful import Resource, reqparse, marshal_with, fields, marshal
from main.api import api
from main.common.hostimpl import host

class HostApi(Resource):
    #decorators = [auth.login_required]

    def get(self):
        host.hello_host()
        return jsonify({'hosts' : 'hello'})

    def post(self):
        pass

api.add_resource(HostApi, '/hosts', endpoint = '/hosts')
