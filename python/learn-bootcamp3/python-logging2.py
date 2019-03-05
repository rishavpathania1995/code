#https://realpython.com/python-logging/

import logging

logger = logging.getLogger(__name__)   # create custom logger

# create handler

file_handler = logging.FileHandler('file.log')
file_handler.setLevel(logging.WARNING)

# create formatter

file_formatter = logging.Formatter('%(name)s-%(levelname)s-%(asctime)s : %(message)s')
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)

logger.warning('hell!!!!')
logger.error('this is error')
