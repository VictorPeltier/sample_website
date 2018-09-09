# /instance/config.py

import os

class Config(object):
    """ Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class DevelopmentConfig(Config):
    """Configuration for development"""
    DEBUG = True

class TestingConfig(Config):
    """Configuration for testing, with a separate test database"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/test-db'
    DEBUG = True

class StagingConfig(Config):
    """Configuration for staging."""
    DEBUG = True

class ProductionConfig(Config):
    """Configuration for Production."""
    DEBUG = False
    TESTING = False

app_config = {
    'development':DevelopmentConfig, 
    'testing':TestingConfig,
    'staging':StagingConfig,
    'production':ProductionConfig
}