#!/usr/bin/env python

from flask_sqlalchemy import SQLAlchemy
import os
from wsgi import app

db = SQLAlchemy(app)

