import bin.ayploader
import os
import getpass
import platform

un = getpass.getuser()

id = 'PS'

while True:
    app = input(f"PoshyWin v0.0.7: {un} {id}> ")
    if "cd" in app:
        try:
            dir = app[3:]
            os.chdir(dir)
        except FileNotFoundError:
            print(f"PoshyWin v0.0.7: {un} {id}> Folder not found!")
            continue
        except OSError:
            print(f"PoshyWin v0.0.7: {un} {id}> Folder not found!")
            continue

    if app == 'exit':
        exit()
    try:
        eval(app)
    except:
        os.system(app)
