#!/usr/bin/env python3
# mandatory blank var because errors
# FIXME: please find a better way to achieve this
CS = ""
from poshy import VERSION, aya, poshcorn
import os
import getpass
os.chdir(os.getenv("HOME"))
un = getpass.getuser()
id = '$'
if un == 'root': # FIXME: this check is bad, check for UID=0 instead
    id = '#'
# TODO: replace this with smth nicer, maybe "[{hostname}@{username}] {curdir}{id} "?
pwd = os.getcwd() #the 'curdir' above is this shit. might need a FIXME later.
PS1 = f"Poshy v{VERSION} | {un} {pwd} {id} "
# if an alternative is detected, make it use that one instead of PS1
if CS in globals():
    PS1 = CS
while True:
    pwd = os.getcwd()
    PS1 = f"Poshy v{VERSION} | {un} {pwd} {id} "
    # if an alternative is detected, make it use that one instead of PS1
    if CS in globals():
        PS1 = CS
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
        # Another thing, we need to change the shell variable.
