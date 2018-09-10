# /instance/config.py

import os

class Config(object):
    """ Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class DevelopmentConfig(Config):
    """Configuration for development"""
    DEBUG = True
    ENV='dev'

class TestingConfig(Config):
    """Configuration for testing, with a separate test database"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/test_db'
    DEBUG = True
    ENV='test'

class StagingConfig(Config):
    """Configuration for staging."""
    DEBUG = True
    ENV='stage'

class ProductionConfig(Config):
    """Configuration for Production."""
    DEBUG = False
    TESTING = False
    ENV='prod'

app_config = {
    'development':DevelopmentConfig, 
    'testing':TestingConfig,
    'staging':StagingConfig,
    'production':ProductionConfig
}