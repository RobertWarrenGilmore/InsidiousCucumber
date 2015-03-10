'''
Created on Jun 19, 2014

@author: Chris
'''
import logging 

from extras import logger

class Config(object):
    DEBUG = False
    TESTING = False
        
class ProdConfig(Config):
    MODE = "Production"
    LOGGER = logger.initLogging('prod.log')
    
class DevConfig(Config):
    DEBUG = True
    MODE = "Development"
    LOGGER = logger.initLogging('dev.log',logging.DEBUG)
    
class TestConfig(Config):
    TEST = False
    MODE = "Testing"
    LOGGER = logger.initLogging('test.log',logging.INFO)
