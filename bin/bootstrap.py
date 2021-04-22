import bin.ayploader
import os
import getpass

un = getpass.getuser()

id = 'PS'

while True:
    app = input(f"Poshy v0.0.7: {un} {id}> ")
    if "cd" in app:
        dir = app[3:]
        os.chdir(dir)
    if app == 'exit':
        exit()
    try:
        eval(app)
    except:
        os.system(app)
