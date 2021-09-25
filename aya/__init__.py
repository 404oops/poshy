from importlib import import_module as load
import os
home = os.getenv("HOME")
try:
    file = open(f"{home}/.aya", 'x')
    file.close()
except FileExistsError:
    pass
file = open(f"{home}/.aya", 'r')
modules = file.read().splitlines()
for module in modules:
    try:
        load(module)
    except ImportError as exception:
        print(exception)
file.close()
