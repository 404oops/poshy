import os
def install(ghuser, ghrepo):
    os.system(f"git clone {ghuser}/{ghrepo} ")
    os.chdir(ghrepo)
    os.system("bash install.sh")
    os.chdir("")
    os.system(f"rm -rf {ghrepo}")