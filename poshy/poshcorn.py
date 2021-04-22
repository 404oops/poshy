import os

def install(ghuser, ghrepo):
    os.system(f"git clone https://github.com/{ghuser}/{ghrepo} ")
    os.chdir(ghrepo)
    os.system("bash install.sh")
    os.chdir("")
    os.system(f"rm -rf {ghrepo}")
