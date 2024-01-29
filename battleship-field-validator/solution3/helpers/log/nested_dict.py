import pathlib, json
class NestedKeyError(KeyError):
    pass

def get_all_keys(d: dict, keys: list=None) -> list[str]:
    """
    get list of all keys in d and nested dicts
    """
    keys = keys or []
    for k, v in d.items():
        keys.append(k)
        if isinstance(v, dict):
            get_all_keys(v, keys)
    return keys

def find_nested_key(d: dict, key: str, keys: list=None) -> list[str]:
    """
    finds nested key inside dict, return the path as a list of keys
    """
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

def find_any_key(d: dict, key: str) -> list[list[str]]:
    """
    return all matching keys and the paths to reach them
    """
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

def find_key(d: dict, key: str, start: list|str|None=None, sep: str='.') -> list[str]:
    """
    find a matching key and returns its path inside dict

    if dict contains more than one key matching, then uses start to choose which one
    if start is not specified and more than one match is found, raises NestedKeyError

    start, if specified, must be a string of 'sep' separated parent keys
    or a list of parent keys

    """
    if not isinstance(start, str|list|type(None)):
        raise TypeError(f'start must be list|str|None')
    elif isinstance(start, list):
        nodes = start[:]
        path = sep.join(start)
    else:
        nodes = sep.split(start)
        path = start
    
    results = find_any_key(d, key)
    
    if start:
        for result in results:
            full = sep.join(result)
            if full.startswith(path):
                return result
        raise NestedKeyError(f'key {key} not found, {start = }')

    if len(results) > 1:
        raise NestedKeyError(f'too many results ({len(results)}): {results}')
    return results[0]


def set_value(d: dict, key,  value, start: str|list|None=None, sep='.') -> None:
    """
    set value for nested key, using start to discriminate between multiple matches
    """
    path = find_key(d, key, start, sep)

    print(f'setting value: {key, value = }, {path = }')
    
    target = d
    for key in path[:-1]:
        target = target[key]
    target[path[-1]] = value

def main():
    def __getconfig():
        config_file = pathlib.Path(__file__).parent / 'logger.json'
        with open(config_file) as f_in:
            config = json.load(f_in)
        return config

    config = __getconfig()
    print(json.dumps(config, indent=2))
    try:
        set_value(config, 'handlers', 'INFO', start='loggers')
        print(json.dumps(config, indent=2))
    except NestedKeyError as nke:
        print(repr(nke))

if __name__ == '__main__':
    main()