import logging
import types

logger = logging.getLogger(__name__)

def args2str(*args, **kwargs) -> str:
    params = list(map(str, args)) + [f'{k}={v}' for k, v in kwargs.items()]
    params = ', '.join(params)
    return params


# def tabbedlogdecorator(tabs=0):
#     _tabs = ' ' * tabs * 4

#     def logdecorator(fn):
#         def wrap(self, *args, **kwargs):
#             params = args2str(*args, **kwargs)
#             print(f'{_tabs}{fn.__name__}({params})')
#             return fn(self, *args, **kwargs)
#         return wrap
#     return logdecorator

def logdecorator(log=logger.debug, strargs=args2str):
    import functools
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            log(f'{func.__name__}({strargs(*args, **kwargs)})')
            result = func(*args, **kwargs)
            log(f'{func.__name__}() returning {result}')
            return result
        return wrapper
    return decorator

def decorate_module_functions(
                        module, 
                        decorator, 
                        strargs=args2str, 
                        *args, **kwargs
    ):
    for name in dir(module):
        obj = getattr(module, name)
        if isinstance(obj, types.FunctionType):
            if args or kwargs:
                setattr(module, name, decorator(strargs, *args, **kwargs)(obj))
            else:
                setattr(module, name, decorator(obj))
