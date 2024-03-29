import logging
import logging.config
import json
import pathlib

from . import nested_dict

SETTINGS_DIR = pathlib.Path(__file__).parent
JSON_PATH = SETTINGS_DIR / 'logger.json'

logger = logging.getLogger(__name__)

def setup_logging(change_value=nested_dict.set_value, start=None, *args, **kwargs) -> dict:
    """
    opens json logging config, changes values if necessary, applies and returns it

    # params

    - change_value: function to change the value of a key in config
    - start       : list of parent keys to the key: ['parent', 'parent'] or 'parent.parent'
    """
    with open(JSON_PATH) as f_in:
        config = json.load(f_in)

    for key, value in kwargs.items():
        change_value(config, key, value, start)

    logging.config.dictConfig(config)
    return config
