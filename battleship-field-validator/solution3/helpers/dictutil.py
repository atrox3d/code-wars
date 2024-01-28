import pathlib, json
class NestedKeyError(KeyError):
    pass

def __getconfig():
    config_file = pathlib.Path(__file__).parent / 'logger.json'
    with open(config_file) as f_in:
        config = json.load(f_in)
    return config


def get_all_keys(d: dict, keys: list=None):
    keys = keys or []
    for k, v in d.items():
        keys.append(k)
        # print(k)
        if isinstance(v, dict):
            get_all_keys(v, keys)
    return keys

def find_nested_key(d: dict, key: str, keys: list=None):
    root = keys is None
    keys = keys or []
    for k, v in d.items():
        if k == key:
            return keys + [k]
        elif isinstance(v, dict):
            if keys := find_nested_key(v, key, keys + [k]):
                return keys
    if not root:
        return []
    raise NestedKeyError(f'find: key {key!r} not found {keys = }')

def find_keys(d, key):
    keys = []
    for k, v in d.items():
        if k == key:
            keys.append([k])
        try:
            if found := find_nested_key(v, key):
                keys.append([k] + found)
        except AttributeError:
            pass
        except NestedKeyError:
            pass
    return keys

def main():
    config = __getconfig()
    print(json.dumps(config, indent=2))
    print(find_keys(config, 'handlers'))

if __name__ == '__main__':
    main()