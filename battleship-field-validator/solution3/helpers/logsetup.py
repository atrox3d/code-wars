import atexit
import json
import logging.config
import logging.handlers
import pathlib

logger = logging.getLogger(__name__)  # __name__ is a common choice

def override(nested: dict, path: str, value, sep='.'):
    path = path.split(sep)
    target = nested
    for key in path[:-1]:
        target = target[key]
    target[path[-1]] = value

def find_path(nested: dict, key: str, path: list=None, sep=None):
    path = path or []

    if key in nested:
        path.append(key)
        return path
    
    for k in nested:
        if isinstance(nested[k], dict):
            if found := find_path(nested[k], key, path + [k]):
                if sep:
                    return sep.join(found)
                return found
    

def setup(**kwargs):
    config_file = pathlib.Path(__file__).parent / 'logger.json'
    with open(config_file) as f_in:
        config = json.load(f_in)


    logging.config.dictConfig(config)
    # queue_handler = logging.getHandlerByName("queue_handler")
    # if queue_handler is not None:
    #     queue_handler.listener.start()
    #     atexit.register(queue_handler.listener.stop)
    return config

if __name__ == '__main__':
    config = setup()
    print(json.dumps(config, indent=4))
    path = find_path(config, 'level', sep='.')
    print(f'path to level = {path}')
    override(config, path, 'INFO')
    print(json.dumps(config, indent=4))