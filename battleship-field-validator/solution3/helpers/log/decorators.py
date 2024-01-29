import logging
import types

logger = logging.getLogger(__name__)

def args2str(max_args_len=None, *args, **kwargs) -> str:
    strargs = list(map(str, args))
    strkwargs = [f'{k}={v}' for k, v in kwargs.items()]
    if max_args_len is not None:
        strargs = [arg[:max_args_len] + '...' if len(arg) > max_args_len else arg for arg in strargs]
        strkwargs = [kwarg[:max_args_len] + '...' if len(kwarg) > max_args_len else kwarg for kwarg in strkwargs]
    params = strargs + strkwargs
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

def logdecorator(log=logger.debug, strargs=args2str, max_args_len=None):
    import functools
    def decorator(func):
        @functools.wraps(func)
        def run_function(*args, **kwargs):
            params = strargs(max_args_len, *args, **kwargs)
            log(f'{func.__name__}({params})')
            result = func(*args, **kwargs)
            log(f'{func.__name__}() returning {result}')
            return result
        return run_function
    return decorator

def decorate_module_functions(
                        module, 
                        decorator, 
                        *args, **kwargs
    ):
    for name in dir(module):
        obj = getattr(module, name)
        if isinstance(obj, types.FunctionType):
            if args or kwargs:
                setattr(module, name, decorator(*args, **kwargs)(obj))
            else:
                setattr(module, name, decorator(obj))
