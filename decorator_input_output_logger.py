#Credit to: https://stackoverflow.com/questions/25936746/create-a-function-decorator-that-logs-arguments
import logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def logger_(prefix):
    def decorate(f):
        def wrapper(*args, **kwargs):
            logger.info(f'{prefix} - {f.__name__} - START')
            logger.info(f'{prefix} - {f.__name__} - INPUT - Positional Args: {args}')
            logger.info(f'{prefix} - {f.__name__} - INPUT - Keyworod Args: {kwargs}')
            output = f(*args, **kwargs)
            logger.info(f'{prefix} - {f.__name__} - OUTPUT: {output}')
            logger.info(f'{prefix} - {f.__name__} - END')
            return output
        return wrapper
    return decorate


@logger("STEP #1")
def zut(a, b, foo='FOO'):
    return a+b
