import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def log_xput(f):
    def wrapper(*args, **kwargs):        
        title = f'RUNNING FUNCTION: {f.__name__}'
        title_n_chars = len(title)
        logger.info(title_n_chars * '=')
        logger.info(title)
        logger.info(title_n_chars * '=')
        logger.info('INPUT'.center(title_n_chars, '-'))
        # log positional args if present
        if len(args) > 0:
            for i, a in enumerate(args):
                logger.info(f'POSITIONAL ARG INPUT - #{i} = {a}')  # should be debug

        # log keyword args if present
        if len(kwargs) > 0:
            for k,v in kwargs.items():
                logger.info(f'KEYWORD ARG INPUT - {k}: {v}')  # should be debug
        logger.info('START'.center(title_n_chars, '-'))
        output = f(*args, **kwargs)
        logger.info('OUTPUT'.center(title_n_chars, '-'))
        logger.info(f'OUTPUT: {output}')  # should be debug
        logger.info('END'.center(title_n_chars, '-'))
        logger.info('\n')
        return output
    return wrapper
  
 
