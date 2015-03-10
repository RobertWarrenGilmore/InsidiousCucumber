import logging, sys


def initLogging(loggerName,loglevel=logging.WARNING):
   
    my_logger = logging.getLogger(loggerName)
    my_logger.setLevel(loglevel)
    
    my_console_handler = logging.StreamHandler()
    my_file_handler = logging.FileHandler('logs/flask.log')
    
    my_formatter = logging.Formatter('%(asctime)s [%(levelname)s]: %(filename)s Line:%(lineno)d\n%(message)s')
    
    my_console_handler.setFormatter(my_formatter)
    my_file_handler.setFormatter(my_formatter)
    
    my_logger.addHandler(my_console_handler)
    my_logger.addHandler(my_file_handler)
    
    return my_logger