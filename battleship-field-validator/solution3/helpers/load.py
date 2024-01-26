import json
import csv
from pathlib import Path

DATA_PATH = Path(__file__).parent.parent / 'data'

def parse_extensions(ext_str:str, separator: str=', '):
    return tuple([f'*.{ext}' for ext in ext_str.split(sep=separator)])

def get_files(*wildcards: tuple[str], extensions: str=None, path: str|Path=DATA_PATH):
    path = Path(path)

    if extensions is not None:
        wildcards += parse_extensions(extensions)

    return [file  for wildcard in [*wildcards] for file in Path(path).glob(wildcard)]

def battlefield(file_path: str|Path):
    loader = get_loader(file_path)
    return loader(file_path)

def get_loader(file_path: str|Path):
    if Path(file_path).suffix == '.ascii':
        return ascii_battlefield
    elif Path(file_path).suffix == '.csv':
        return csv_battlefield
    elif Path(file_path).suffix == '.json':
        return json_battlefields
    else:
        raise NotImplementedError(f'unknown extension {Path(file_path).suffix}')

def json_battlefields(file_path: str|Path):
    with open(file_path, 'r') as fp:
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
def csv_battlefield(file_path: str|Path):
    with open(file_path, newline='') as file:
        reader = csv.reader(file)
        battlefield =  [[char.strip() if char.strip() in '01' else char for char in line] for line in reader ]
        return battlefield

@non_json_adapter
def ascii_battlefield(file_path: str|Path):
    with open(file_path) as fp:
        battlefield = [[cell for cell in list(line.rstrip('\n'))] for line in fp]
    return battlefield
