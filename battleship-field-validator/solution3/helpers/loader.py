import json
import csv
from pathlib import Path

DATA_PATH = Path(__file__).parent.parent / 'data'

def parse_extensions(ext_str:str, separator=', '):
    return tuple([f'*.{ext}' for ext in ext_str.split(sep=separator)])

def get_files(*wildcards, extensions=None, path=DATA_PATH):
    path = Path(path)

    if extensions is not None:
        wildcards += parse_extensions(extensions)

    return [file  for wildcard in [*wildcards] for file in Path(path).glob(wildcard)]

def load_battlefield(file):
    loader = get_loader(file)
    return loader(file)

def get_loader(file):
    if Path(file).suffix == '.ascii':
        return load_ascii_battlefield
    elif Path(file).suffix == '.csv':
        return load_csv_battlefield
    elif Path(file).suffix == '.json':
        return load_json_battlefields
    else:
        raise NotImplementedError(f'unknown extension {Path(file).suffix}')

def load_json_battlefields(filename):
    with open(filename, 'r') as fp:
        tests = json.load(fp)
        return tests

def non_json_adapter(func):
    def wrapper(filename):
        battlefield = func(filename)
        return [{
                'name': Path(filename).name,
                'data': battlefield,
                'expected': 'unknown'
            }]
    return wrapper

@non_json_adapter
def load_csv_battlefield(filename: str):
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        battlefield =  [[char.strip() if char.strip() in '01' else char for char in line] for line in reader ]
        return battlefield

@non_json_adapter
def load_ascii_battlefield(filename: str):
    with open(filename) as fp:
        battlefield = [[cell for cell in list(line.rstrip('\n'))] for line in fp]
    return battlefield
