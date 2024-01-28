import logging
import logging.config
import json
import pathlib

from . import nested_dict

def setup(change=nested_dict.set_value, *args, **kwargs):
    config_file = pathlib.Path(__file__).parent / 'logger.json'
    with open(config_file) as f_in:
        config = json.load(f_in)

    for key, value in kwargs.items():
        change(config, key, value)

    logging.config.dictConfig(config)
    return config
        