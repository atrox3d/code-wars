import atexit
import json
import logging.config
import logging.handlers
import pathlib

logger = logging.getLogger(__name__)  # __name__ is a common choice

def override(config: dict, path: str, value, sep='.'):
    path = path.split(sep)
    target = config
    for key in path[:-1]:
        target = target[key]
    target[path[-1]] = value

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
    print(config)
    override(config, 'loggers.root.level', 'INFO')
    print(config)
