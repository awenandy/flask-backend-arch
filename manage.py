#!/usr/bin/env python

import multiprocessing

from main.wsgi import app
from main.wsgi import init_app, register_extensions

init_app( )

from main.common.userimpl import new_user
from main.testdb import testdb
from main.database import db

register_extensions(app,db)
new_user()
testdb.checkpassword()

if __name__ == '__main__':
    multiprocessing.freeze_support()
    app.run(port=8003)
