""" Created on Jun 19, 2014

@author: Chris
"""

import logging 

from extras import logger


class Config(object):
    DEBUG = False
    TESTING = False
    MONGODB_SETTINGS = {
        'db': 'minerva',
        'host': 'mongodb://minerva-admin:mitigating@dbh62.mongolab.com:27627/minerva'
    }
    SECRET_KEY = 'SomeSuperSecretKeyNoOneShouldBeAbleToGuess'


class ProdConfig(Config):
    MODE = "Production"
    # LOGGER = logger.initLogging('flask')
    APP_LOGGER = logger.init_logging('prod.log')


class DevConfig(Config):
    DEBUG = True
    MODE = "Development"
    # LOGGER = logger.initLogging('flask',logging.DEBUG)
    APP_LOGGER = logger.init_logging('dev.log', logging.DEBUG)


class TestConfig(Config):
    DEBUG = False
    TESTING = True
    MODE = "Testing"
    # LOGGER = logger.initLogging('flask',logging.INFO)
    APP_LOGGER = logger.init_logging('test.log')
