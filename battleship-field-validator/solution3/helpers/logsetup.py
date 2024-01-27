# import atexit
import json
import logging.config
# import logging.handlers
import pathlib

logger = logging.getLogger(__name__)  # __name__ is a common choice

def override(nested: dict, path: str, value, sep='.'):
    path = path.split(sep)
    target = nested
    for key in path[:-1]:
        target = target[key]
    target[path[-1]] = value

def find_path(nested: dict, key: str, path: list=None, sep='.'):
    path = path or []
    found = None    
    for k in nested:
        if key == k:
            found = path + [k]
            break
        elif isinstance(nested[k], dict):
            if found := find_path(nested[k], key, path + [k]):
                break
    else:
        if not path: # root of dict, path is []
            raise KeyError(f'key {key!r} not found')

    if found and not path: # root of dict, path is []
        if sep: 
            # return 'sep' separated string
            return sep.join(found)
    # return list
    return found


def setup(**kwargs):
    config_file = pathlib.Path(__file__).parent / 'logger.json'
    with open(config_file) as f_in:
        config = json.load(f_in)

    for key, value in kwargs.items():
        path = find_path(config, key)
        override(config, path, value)
    
    logging.config.dictConfig(config)
    # queue_handler = logging.getHandlerByName("queue_handler")
    # if queue_handler is not None:
    #     queue_handler.listener.start()
    #     atexit.register(queue_handler.listener.stop)
    return config

if __name__ == '__main__':
    config = setup(level='INFO')
    # path = find_path(config, 'level')
    # print(f'path to level = {path}')
    # override(config, path, 'INFO')
    print(json.dumps(config, indent=1 ))