def param2str(*args, **kwargs) -> str:
    params = list(map(str, args)) + [f'{k}={v}' for k, v in kwargs.items()]
    params = ', '.join(params)
    return params     

def exercise_runner(params_to_string=param2str):
    def arg_wrapper(func):
        import functools
        @functools.wraps(func)
        def function_wrapper(*args, **kwargs):
            params = params_to_string(*args, **kwargs)
            print(f'running {func.__name__}({params})')
            result = func(*args, **kwargs)
            print(f'{result = }')
            return result
        return function_wrapper
    return arg_wrapper

def info_decorator(func, param_formatter, *args, **kwargs):
        params = param_formatter(*args, **kwargs)
        print(f'running {func.__name__}({params})')
        result = func(*args, **kwargs)
        print(f'{result = }')
        return result

def run(
            func, 
            *args, 
            param_formatter=param2str,
            print_run_info=True,
            info_decorator=info_decorator, 
            **kwargs
        ):
    if print_run_info:
        result = info_decorator(func, param_formatter, *args, **kwargs)
    else:
         result = func(*args, **kwargs)
    return result
