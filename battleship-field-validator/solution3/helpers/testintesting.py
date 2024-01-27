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
    if isinstance(path, str):
        path = path.split(sep)
        # *path, key= key.split(sep)
        start = nested
        for node in path:
            start = start[node]
        
        print(f'{start = }, {path = }, {key = }')
        found =  path_to_key(start, key, path)
        if not found:
            raise NestedKeyError(f'key {key!r} not found {path = }')
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
            raise NestedKeyError(f'key {key!r} not found {path = }')

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

def traverse(d, keys=None):
    keys = keys or []
    for k, v in d.items():
        # print(f'{k, v = }')
        keys.append(k)
        print(k)
        if isinstance(v, dict):
            # print(f'traversing {v}')
            traverse(v, keys)
    # print(path)
    return keys

if __name__ == '__main__':
    config = setup()
    print(json.dumps(config, indent=1))
    keys = traverse(config)
    print(keys)

    for key in keys:
        path = path_to_key(config, key)
        print(f'{path = }')
