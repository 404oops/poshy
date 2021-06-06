from . import aya, poshcorn
import os, shlex, subprocess
mirror = "404oops.ml/poshcorn"
VERSION = 0.4
### VERSION SYSTEM]
# BY DEFAULT AUTO-UPDATES ARE ON, PLEASE TURN IT OFF IF YOU DONT WANT AUTO-UPDATES
au = 1
import shlex, subprocess
cmd = "curl -s http://404oops.ml/poshcorn/version"
d = subprocess.getoutput(cmd)
d = d[2:]
d = float(d)
if d > VERSION:
    print(f"This version of poshy is outdated, please download the newer version of Poshy at Github (Current version: {VERSION}, new: {d})")
    if au == 1:
        gp = "git pull"
        gp = shlex.split(gp)
        subprocess.run(gp)
    elif au == 0:
        print("")