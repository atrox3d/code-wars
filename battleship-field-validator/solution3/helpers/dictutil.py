import pathlib, json
class NestedKeyError(KeyError):
    pass

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

def find_key(d: dict, key: str, start: list|str|type(None)=None, sep: str='.'):
    # start = start or ''
    if not isinstance(start, str|list|type(None)):
        raise TypeError(f'start must be list|str|None')
    elif isinstance(start, list):
        nodes = start[:]
        path = sep.join(start)
    else:
        nodes = sep.split(start)
        path = start
    
    results = find_keys(d, key)
    
    if start:
        for result in results:
            full = sep.join(result)
            if full.startswith(path):
                return result
        raise NestedKeyError(f'key {key} not found, {start = }')

    if len(results) > 1:
        raise NestedKeyError(f'too much results ({len(results)}): {results}')
    return results

def main():
    def __getconfig():
        config_file = pathlib.Path(__file__).parent / 'logger.json'
        with open(config_file) as f_in:
            config = json.load(f_in)
        return config

    config = __getconfig()
    print(json.dumps(config, indent=2))
    try:
        print(find_key(config, 'handlers', start='formatters'))
    except NestedKeyError as nke:
        print(repr(nke))

if __name__ == '__main__':
    main()