import sys
from logging import getLogger, StreamHandler, Formatter, WARNING
from logging.handlers import RotatingFileHandler

LOG_FILENAME = 'logs/flask.log'

def initLogging(loggerName,loglevel=WARNING):
   
    my_logger = getLogger(loggerName)
    my_logger.setLevel(loglevel)
    
    my_console_handler = StreamHandler()
    my_file_handler = RotatingFileHandler(LOG_FILENAME, mode='w', maxBytes=1000, backupCount=3)
    
    my_formatter = Formatter('%(asctime)s [%(levelname)s]: %(filename)s Line:%(lineno)d\n%(message)s')
    
    my_console_handler.setFormatter(my_formatter)
    my_file_handler.setFormatter(my_formatter)
    
    my_logger.addHandler(my_console_handler)
    my_logger.addHandler(my_file_handler)
    
    return my_logger