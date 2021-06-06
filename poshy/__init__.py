from . import aya, poshcorn
import os, shlex, subprocess
mirror = "404oops.ml/poshcorn"
VERSION = 0.5
### VERSION SYSTEM]
# BY DEFAULT AUTO-UPDATES ARE ON, PLEASE TURN IT OFF IF YOU DONT WANT AUTO-UPDATES
au = 1
import shlex, subprocess
cmd = "curl -s http://404oops.ml/poshcorn/version"
d = subprocess.getoutput(cmd)
d = d[2:]
d = float(d)
if d > VERSION:
    if au == 1:
        print("Updating..")
        gp = "git pull"
        if subprocess.getoutput(gp) == "Already up to date.":
            gp = shlex.split(gp)
            subprocess.run(gp)
        else:
            gp = shlex.split(gp)
            subprocess.run(gp)
            print("Updated!")
    elif au == 0:
        print(f"This version of poshy is outdated, please download the newer version of Poshy at Github (Current version: {VERSION}, new: {d})")