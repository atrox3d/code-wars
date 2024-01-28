class NestedKeyError(KeyError):
    pass

def get_all_keys(d, keys=None):
    keys = keys or []
    for k, v in d.items():
        keys.append(k)
        # print(k)
        if isinstance(v, dict):
            get_all_keys(v, keys)
    return keys


def find(d, key, keys=None):
    root = keys is None
    keys = keys or []
    for k, v in d.items():
        if k == key:
            return keys + [k]
        elif isinstance(v, dict):
            if keys := find(v, key, keys + [k]):
                return keys
    if not root:
        return []
    raise NestedKeyError(f'find: key {key!r} not found {keys = }')
