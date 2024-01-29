import logging

logger = logging.getLogger(__name__)

def logdecorator(log=logger.debug):
    import functools
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            log(f'{func.__name__}({args=}, {kwargs=})')
            result = func(*args, **kwargs)
            log(f'{func.__name__}() returning {result}')
            return result
        return wrapper
    return decorator

def decorate_all_in_module(module, decorator):
    for name in dir(module):
        obj = getattr(module, name)
        if isinstance(obj, types.FunctionType):
            setattr(module, name, decorator(obj))
