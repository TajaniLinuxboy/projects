import logging
logging.basicConfig(filename="app.log", format="%(asctime)s %(message)s", filemode='a')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)