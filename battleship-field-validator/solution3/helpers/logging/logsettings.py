import logging
import logging.config
import json
import pathlib

from . import nested_dict

SETTINGS_DIR = pathlib.Path(__file__).parent
JSON_PATH = SETTINGS_DIR / 'logger.json'

def setup(change_value=nested_dict.set_value, *args, **kwargs):
    with open(JSON_PATH) as f_in:
        config = json.load(f_in)

    for key, value in kwargs.items():
        change_value(config, key, value)

    logging.config.dictConfig(config)
    return config
