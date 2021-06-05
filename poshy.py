#!/usr/bin/env python3
CS = ""
from poshy import VERSION, aya, poshcorn, hlp
import os, getpass, socket, subprocess, shlex
os.chdir(os.getenv("HOME"))
un = getpass.getuser()
hn = socket.gethostname()
if ".local" in hn:
    hn = hn[:-6]
id = '$'
if un == 'root':
    id = '#'
    print("Poshy is unstable on root, because you may type something wrong and it may be irreversible. Proceed with caution")
print(f"Poshy v{VERSION}")
pwd = os.getcwd()
while True:
    pwd = os.getcwd()
    if "/Users/" in pwd:
        pwd = pwd[6:]
        pwd = f"~{pwd}"
    if "/home/" in pwd:
        pwd = pwd[5:]
        pwd = f"~{pwd}"
    PS1 = f"[{un}@{hn}] {pwd} {id} "
    if CS in globals():
        PS1 = CS
    app = input(PS1)
    if "cd" in app:
        dir = app[3:]
        os.chdir(dir)
    if app == 'exit':
        exit()
    if app == 'help':
        hlp.twhlp()
    try:
        exec(app)
    except:
        app = shlex.split(app)
        subprocess.run(app)