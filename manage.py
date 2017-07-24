#!/usr/bin/env python

from main.wsgi import app
from main.wsgi import init_app
from main.database import db
from main.common.userimpl import new_user
from main.testdb import testdb

init_app(db)
new_user()
testdb.checkpassword()

if __name__ == '__main__':
     app.run(port=8003)
