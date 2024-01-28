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

def find_key(d: dict, key: str, start: list|str|None=None, sep: str='.'):
    results = find_keys(d, key)

    if len(results) > 1:
        raise NestedKeyError(f'too much results ({len(results)}): {results}')
    return results

def __find_key(d, key, start=None, sep='.'):
    str_path = ''
    list_path = []
    if start:
        if isinstance(start, str):
            str_path =  start
            list_path = start.split(sep)
        elif isinstance(start, list):
            str_path = sep.join(start)
            list_path = start
        elif start is not None:
            raise ValueError(f'start must be None|str|list: {start=}')

        for node in list_path:
            try:
                d = d[node]
                print(f'starting from {node = }: {d =}')
                paths = find_keys(d, key)
                for path in paths:
                    print(f'{list_path + path = }')
                    path = list_path + path
            except KeyError:
                raise NestedKeyError(f'invalid start {start}')
    else:    
        paths = find_keys(d, key)
    print(f'{paths = }')
    print(f'{list_path = }')
    if list_path:
        for path in paths:
            print(f'{path = }')
            print(f'{path[:len(list_path)] = }')
            if path[:len(list_path)] == list_path:
                return path
        raise NestedKeyError(f'key {key!r} not found')
    return paths

def main():
    def __getconfig():
        config_file = pathlib.Path(__file__).parent / 'logger.json'
        with open(config_file) as f_in:
            config = json.load(f_in)
        return config

    config = __getconfig()
    print(json.dumps(config, indent=2))
    try:
        print(find_key(config, 'handlers'))
    except NestedKeyError as nke:
        print(repr(nke))

if __name__ == '__main__':
    main()