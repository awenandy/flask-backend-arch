#!/usr/bin/env python
import os

class Config(object):
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))

    ERROR_404_HELP = False



class ProdConfig(Config):
    """Production configuration."""
    ENV = 'prod'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db3.sqlite'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

class DevConfig(Config):
    """Development configuration."""
    #SECRET_KEY = 'test'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db3.sqlite'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

class TestConfig(Config):
    """Test configuration."""
    ENV = 'test'
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
