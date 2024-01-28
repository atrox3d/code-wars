import json
import logging.config
import pathlib

import dictutil
import recursion
import nested

logger = logging.getLogger(__name__)  # __name__ is a common choice


def setup(**kwargs):
    config_file = pathlib.Path(__file__).parent / 'logger.json'
    with open(config_file) as f_in:
        config = json.load(f_in)

    for key, value in kwargs.items():
        nested.update_config_value(config, key, value)

    logging.config.dictConfig(config)
    return config
        
if __name__ == '__main__':
    config = setup()
    print(json.dumps(config, indent=1))
    keys = recursion.traverse(config)
    keys.append('error man!')
    print(keys)
    # print(find(config, 'stream'))
    # print(path_to_key(config, 'stream'))

    # exit()
    for key in keys:
        try:
            found = dictutil.find(config, key)
            print(f'{found = }')
        except dictutil.NestedKeyError as ne:
            print(repr(ne))
        try:
            pathtokey = nested.path_to_key(config, key)
            print(f'{pathtokey = }')
        except dictutil.NestedKeyError as ne:
            print(repr(ne))
        print()
