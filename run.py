import sys
import importlib.util
from pathlib import Path

path = Path(sys.argv[1])

if path.is_dir():
    path = path / 'exercise.py'


# specify the module that needs to be 
# imported relative to the path of the 
# module
spec=importlib.util.spec_from_file_location(
                        "exercise",
                        path)

# creates a new module based on spec
foo = importlib.util.module_from_spec(spec)

# executes the module in its own namespace
# when a module is imported or reloaded.
spec.loader.exec_module(foo)


foo.main()
