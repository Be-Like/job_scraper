import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
  DEBUG = False
  TESTING = False
  CSRF_ENABLED = True
  SCRAPY_SETTINGS_MODULE = os.environ['SCRAPY_SETTINGS']
  SECRET_KEY = 'this-is-not-so-secret'
  SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class ProductionConfig(object):
  DEBUG = False


class StagingConfig(object):
  DEBUG = True
  DEVELOPMENT = True


class DevelopmentConfig(object):
  DEBUG = True
  DEVELOPMENT = True
  SCRAPY_SETTINGS_MODULE = os.environ['SCRAPY_SETTINGS']
  SECRET_KEY = os.environ['SECRET_KEY']
  SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class TestingConfig(Config):
  TESTING = True
