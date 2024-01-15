import sys
import importlib.util

# specify the module that needs to be 
# imported relative to the path of the 
# module
spec=importlib.util.spec_from_file_location("gfg",f"{sys.argv[1]}/exercise.py")

# creates a new module based on spec
foo = importlib.util.module_from_spec(spec)

# executes the module in its own namespace
# when a module is imported or reloaded.
spec.loader.exec_module(foo)


foo.main()
