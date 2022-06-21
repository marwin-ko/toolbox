def my_timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        f = func(*args, **kwargs)
        end = round(time.time(),2)
        logger.info("Data Transfer Duration: %s sec", end - start)
        return f
    return wrapper
