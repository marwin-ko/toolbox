# Reference
# https://www.logicmonitor.com/blog/python-logging-levels-explained#logging-levels
# https://docs.python.org/3/howto/logging.html


# Levels (warning and higher are logged by default)
# 0 - DEBUG
# 1 - INFO
# 2 - WARNING (default)
# 3 - ERROR
# 4 - CRITICAL


import logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


logger.debug('This is a known bug. Here are some solutions.')
logger.info('This is info.')
logger.warning('This is a warning.')
logger.error('This is an error.')
logger.critical('This is a critical error...')
