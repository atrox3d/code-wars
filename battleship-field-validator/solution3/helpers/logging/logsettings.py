import logging
import logging.config
import json
import pathlib

from . import nested_dict

SETTINGS_DIR = pathlib.Path(__file__).parent
JSON_PATH = SETTINGS_DIR / 'logger.json'

def setup(change=nested_dict.set_value, *args, **kwargs):
    config_file =  JSON_PATH
    with open(config_file) as f_in:
        config = json.load(f_in)

    for key, value in kwargs.items():
        change(config, key, value)

    logging.config.dictConfig(config)
    return config
