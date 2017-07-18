#!/usr/bin/env python

from main.models.user import User
from main.database import db

class TestCase():
    def checkpassword(self):
        u = User.query.filter_by(username ='flask').first()
        print 'username %s \n' % u.username
        print 'password %s \n' % u.password_hash

testdb =TestCase()