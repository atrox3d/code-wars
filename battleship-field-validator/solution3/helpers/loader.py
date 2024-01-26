import json
import csv
from pathlib import Path

def get_files(path, *wildcards):
    path = Path(path)
    return [file  for wildcard in [*wildcards] for file in Path(path).glob(wildcard)]

def load_file(file):
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

def load_csv_battlefield(filename: str):
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        battlefield =  [[char.strip() if char.strip() in '01' else char for char in line] for line in reader ]
        return battlefield

def load_ascii_battlefield(filename: str):
    with open(filename) as fp:
        battlefield = [[cell for cell in list(line.rstrip('\n'))] for line in fp]
    return battlefield
