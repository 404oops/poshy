import os
mirror = "66.79.166.101/poshcorn"
pcd = os.getcwd()
def install(pkg):
    cud = os.getcwd()
    os.chdir(pcd)
    os.system(f"wget 'http://{mirror}/{pkg}/install.sh"'')
    os.system("bash install.sh")
    os.system("rm install.sh")
    os.chdir(cud)