import logging

log_config = logging.basicConfig(filename='auth.log', format='%(asctime)s %(message)s', filemode='r+')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
