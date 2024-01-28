import dictutil

def set_nested_value(nested: dict, path: str, value, sep='.'):
    if isinstance(path, str):
        path = path.split(sep)
    target = nested
    for key in path[:-1]:
        target = target[key]
    target[path[-1]] = value

def path_to_key(nested: dict, key: str, path: list=None, sep='.'):
    path = path or []
    if isinstance(path, str):
        path = path.split(sep)
        # *path, key= key.split(sep)
        start = nested
        for node in path:
            start = start[node]
        
        print(f'{start = }, {path = }, {key = }')
        found =  path_to_key(start, key, path)
        if not found:
            raise dictutil.NestedKeyError(f'path_to_key: key {key!r} not found {path = }')
        else:
            return found
    
    found = None
    for k in nested:
        if key == k:
            found = path + [k]
            break
        elif isinstance(nested[k], dict):
            if found := path_to_key(nested[k], key, path + [k]):
                break
    else:
        if not path: # root of dict, path is []
            raise dictutil.NestedKeyError(f'path_to_key: key {key!r} not found {path = }')

    if found and not path: # root of dict, path is []
        if sep: 
            # return 'sep' separated string
            return sep.join(found)
    # return list
    return found

def update_config_value(config, key, value):
    path = path_to_key(config, key)
    set_nested_value(config, path, value)
