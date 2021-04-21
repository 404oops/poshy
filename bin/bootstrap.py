import bin.ayploader
import os
import getpass
un = getpass.getuser()
id = '$'
if un == 'root':
    id = '#'
while True:
    app = input(f"Poshy: {un} {id}> ")
    if app == 'exitos':
        exit()
    try:
        eval(app)
    except:
        os.system(app)
