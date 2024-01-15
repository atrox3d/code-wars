def param2str(*args, **kwargs) -> str:
    params = list(map(str, args)) + [f'{k}={v}' for k, v in kwargs.items()]
    params = ', '.join(params)
    return params     

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
