import logging
import time


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def function_timer(f):
    def wrapper(*args, **kwargs):
        title = f'RUNNING FUNCTION: {f.__name__}'
        title_n_chars = len(title)
        logger.info(title_n_chars * '=')
        logger.info(title)
        logger.info(title_n_chars * '=')
        start = time.time()
        output = f(*args, **kwargs)
        end = round(time.time(),2)
        logger.info("Total Function Run Duration: %s sec", end - start)
        logger.info(title_n_chars * '=')
        return output
    return wrapper
