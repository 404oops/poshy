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
    try:
        pwd = os.getcwd()
        if os.getenv("HOME") in pwd:
            al = os.getenv("HOME")
            va = len(al)
            pwd = pwd[va:]
            pwd = f"~{pwd}"
        PS1 = f"[{un}@{hn}] {pwd} {id} "
        if CS in globals():
            PS1 = CS
        app = input(PS1)
        if "cd" in app[0:2]:
            try:
                dir = app[3:]
                if dir == '':
                    os.chdir(os.getenv("HOME"))
                    continue
                os.chdir(dir)
            except:
                print(f"Directory '{dir}' has not been found.")
                continue
        if app == ('exit'):
            exit()
        if app == 'exit()':
            exit()
        if app == 'help':
            hlp.twhlp()
        try:
            exec(app)
        except:
            try:
                if 'cd' in app:
                    continue
                app = shlex.split(app)
                subprocess.run(app)
            except:
                if 'cd' in app:
                    continue
                else:
                    print("Syntax error")
                    continue
    except KeyboardInterrupt:
        print("\n")
        continue