from . import aya, poshcorn
mirror = "404oops.ml/poshcorn"
VERSION = 0.2
### VERSION SYSTEM
import shlex, subprocess
cmd = "curl -s http://404oops.ml/poshcorn/version"
d = subprocess.getoutput(cmd)
d = d[2:]
d = float(d)
if d > VERSION:
    print(f"This version of poshy is outdated, please download the newer version of Poshy at Github (Current version: {VERSION}, new: {d})")
