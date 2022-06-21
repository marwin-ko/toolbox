# Reference
# https://www.logicmonitor.com/blog/python-logging-levels-explained#logging-levels
# https://docs.python.org/3/howto/logging.html
# https://stackoverflow.com/questions/4874335/does-anyone-really-use-warn-as-a-logging-level
# https://www.machinelearningplus.com/python/python-logging-guide/

# Levels (warning and higher are logged by default)
# 0 - DEBUG
# 1 - INFO
# 2 - WARNING (default)
# 3 - ERROR
# 4 - CRITICAL


import logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


logger.debug('Very detailed information for diagnostic purposes. -- What is going on?')
logger.info('Logging information on successful executioned block(s) of code. -- What step did we complete?')
logger.warning('Program can still run, but has detected ODD BEHAVIOR. -- What odd behavior is seen?')
logger.error('Program is unable to run because of a KNOWN ERRORS that are recoverable (e.g. no data loss). -- Why did it stop?')
logger.critical('Program is unable to run due to an UNRECOVERABLE ERROR (e.g. data loss. -- FML...')
