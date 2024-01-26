import atexit
import json
import logging.config
import logging.handlers
import pathlib

logger = logging.getLogger(__name__)  # __name__ is a common choice


def setup(**kwargs):
    config_file = pathlib.Path(__file__).parent / 'logger.json'
    with open(config_file) as f_in:
        config = json.load(f_in)

    logging.config.dictConfig(config)
    logging.basicConfig(**kwargs)
    # queue_handler = logging.getHandlerByName("queue_handler")
    # if queue_handler is not None:
    #     queue_handler.listener.start()
    #     atexit.register(queue_handler.listener.stop)
