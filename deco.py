def log(func):
    def wrapper(*args, **kwargs):
        print "in log1"
        return func(*args, **kwargs)
    return wrapper


def log2(param):
    def deco(func):
        def wrapper(*args, **kwargs):
            print "in log 2 and param is {0}".format(param)
            return func(*args, **kwargs)
        return wrapper
    return deco


def log3(param):
    def wrapper(*args, **kwargs):
        print "in log3 and no param"
        return param(*args, **kwargs)

    def deco(func):
        def wrapper(*args, **kwargs):
            print "in log3 and param is {0}".format(param)
            return func(*args, **kwargs)
        return wrapper

    if callable(param):
        return wrapper
    else:
        return deco
