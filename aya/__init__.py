from importlib import import_module as load
import os
home = os.getenv("HOME")
file = open(f"{home}/.aya", 'a+')
modules = file.read().splitlines()
for module in modules:
    try:
        load(module)
    except ImportError as exception:
        print(exception)
file.close()
