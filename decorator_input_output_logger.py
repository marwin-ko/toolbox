#Credit to: https://stackoverflow.com/questions/25936746/create-a-function-decorator-that-logs-arguments

def logger(prefix):
    def decorate(f):
        def wrapper(*args, **kwargs):
            print(prefix, f.__name__, "args", args, "kwargs", kwargs)
            cr = f(*args, **kwargs)
            print(prefix, f.__name__, "result", cr)
            return cr
        return wrapper
    return decorate


@logger("test")
def zut(a, b, foo='FOO'):
    return a+b
