import os
# needs improvement.
mirror = "404oops.ml/poshcorn"
pcd = os.getcwd()
def install(pkg):
    cud = os.getcwd()
    os.chdir(pcd)
    os.system(f"wget 'https://{mirror}/{pkg}/install.sh'")
    os.system("bash install.sh")
    os.system("rm install.sh")
    os.chdir(cud)
