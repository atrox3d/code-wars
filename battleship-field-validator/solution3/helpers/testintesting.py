import json
import logging.config

import dictutil
import recursion
import nested
import log

logger = logging.getLogger(__name__)  # __name__ is a common choice


if __name__ == '__main__':
    config = log.setup()
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
