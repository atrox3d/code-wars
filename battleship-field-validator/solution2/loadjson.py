import json
from pathlib import Path

path = Path(__file__).parent / 'tests.formatted.json'

with open(path, 'r') as fp:
    tests = json.load(fp)

print(tests)