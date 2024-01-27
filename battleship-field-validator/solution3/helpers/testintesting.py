import json
import logging.config
import pathlib

logger = logging.getLogger(__name__)  # __name__ is a common choice

class NestedKeyError(KeyError):
    pass

def set_nested_value(nested: dict, path: str, value, sep='.'):
    if isinstance(path, str):
        path = path.split(sep)
    target = nested
    for key in path[:-1]:
        target = target[key]
    target[path[-1]] = value

def path_to_key(nested: dict, key: str, path: list=None, sep='.'):
    path = path or []
    if sep in key:
        *path, key= key.split(sep)
        start = nested
        for node in path:
            start = start[node]
        
        print(f'{start = }, {path = }, {key = }')
        return path_to_key(start, key, path)
    elif isinstance(path, str):
        path = path.split(sep)
    
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
            raise NestedKeyError(f'key {key!r} not found')

    if found and not path: # root of dict, path is []
        if sep: 
            # return 'sep' separated string
            return sep.join(found)
    # return list
    return found

def update_config_value(config, key, value):
    path = path_to_key(config, key)
    set_nested_value(config, path, value)

def setup(**kwargs):
    config_file = pathlib.Path(__file__).parent / 'logger.json'
    with open(config_file) as f_in:
        config = json.load(f_in)

    for key, value in kwargs.items():
        update_config_value(config, key, value)

    logging.config.dictConfig(config)
    return config

if __name__ == '__main__':
    config = setup()
    print(json.dumps(config, indent=1))
    path = path_to_key(config, 'loggers.root.handlers')
    print(f'{path = }')
