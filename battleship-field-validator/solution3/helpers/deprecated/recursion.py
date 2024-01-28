
def traverse(d, keys=None):
    keys = keys or []
    for k, v in d.items():
        keys.append(k)
        print(k)
        if isinstance(v, dict):
            traverse(v, keys)
    return keys
