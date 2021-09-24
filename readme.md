<p align="center">
	<img title="Poshy" alt="Poshy" src="images/poshy-logo-shadowed.png" width="256">
	<h1>Poshy, an extensible shell written in Python</h1>
</p>

You can contact us via [our Discord!](https://discord.gg/R5ExvA63Jz)

Poshy is a work-in-progress shell written in Python. As of now, it has no configuration files.

To install, just clone this repo and then run `pip3 install .` and presto!

For aya developers:

AYA is an extensive python module loader that loads before start. You must have them installed as python modules.
```python
from setuptools import setup
setup(
    name='youraddonname',
    packages=['folder'], # the folder in which your __init__.py file is stored in, also must be your addon name
    version='1.0', # self-explanatory
    description='the addon description'
)
```
here's a dummy example of what your setup.py should have. note that to load the addon, you must first install it and then put its name in ~/.aya

your `__init__.py` is your addon

~/.aya's structure goes as following:

modules must be line separated (no commas, no same-line whitespace separated things...)

an example would be:

```
module1
module2
module3
```
and so on.