from setuptools import setup
setup(
    name='poshy',
    packages=['aya'],
    version='1.7',
    description='An extensible shell written in python',
    long_description="""<p align="center">\n\t<a href="https://discord.gg/R5ExvA63Jz"><img title="Poshy" alt="Poshy" src="images/poshy-logo-shadowed.png" width="256"></a>\n\t<h1>Poshy, an extensible shell written in Python</h1>\n</p>\n\nPoshy is a work-in-progress shell written in Python. As of now, it has no configuration files.\n\nTo install, just clone this repo and then run `pip3 install .` and presto!\n\nFor aya developers:\n\nAYA is an extensive python module loader that loads before start. You must have them installed as python modules.\n```python\nfrom setuptools import setup\nsetup(\n    name='youraddonname',\n    packages=['folder'], # the folder in which your __init__.py file is stored in, also must be your addon name\n    version='1.0', # self-explanatory\n    description='the addon description'\n)\n```\nhere's a dummy example of what your setup.py should have. note that to load the addon, you must first install it and then put its name in ~/.aya\n\nyour `__init__.py` is your addon\n\n~/.aya's structure goes as following:\n\nmodules must be line separated (no commas, no same-line whitespace separated things...)\n\nan example would be:\n\n```\nmodule1\nmodule2\nmodule3\n```\nand so on.""",
    long_description_content_type='text/markdown',
    scripts=['bin/poshy']
)