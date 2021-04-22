import bin.ayploader
import os
import getpass
un = getpass.getuser()
id = '$'
if un == 'root':
    id = '#'
while True:
    app = input(f"Poshy v0.0.7: {un} {id}> ")
    if "cd" in app:
        dir = app[3:]
        os.chdir(dir)
    if app == 'exitos':
        exit()
    try:
        exec(app)
    except:
        os.system(app)
