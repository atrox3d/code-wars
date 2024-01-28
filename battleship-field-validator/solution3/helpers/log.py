import logging
import json
import pathlib

import nested

def setup(change_value=nested.update_config_value, *args, **kwargs):
    config_file = pathlib.Path(__file__).parent / 'logger.json'
    with open(config_file) as f_in:
        config = json.load(f_in)

    for key, value in kwargs.items():
        nested.update_config_value(config, key, value)

    logging.config.dictConfig(config)
    return config
        