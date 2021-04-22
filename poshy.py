#!/usr/bin/env python3
from poshy import VERSION, aya, poshcorn
import os
import getpass

un = getpass.getuser()
id = '$'
if un == 'root': # FIXME: this check is bad, check for UID=0 instead
    id = '#'
# TODO: replace this with smth nicer, maybe "[{hostname}@{username}] {curdir}{id} "?
PS1 = f"Poshy v{VERSION} | {un} {id} "

while True:
    app = input(PS1)
    if "cd" in app:
        dir = app[3:]
        os.chdir(dir)
    if app == 'exit':
        exit()
    try:
        eval(app) # FIXME: this is stupid
    except:
        os.system(app) # FIXME: this relies on an another shell, trash
