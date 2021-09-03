import os
import platform
import time

MSG_PATH = os.path.join(os.path.dirname(__file__), ".motd")

if not os.path.exists(MSG_PATH):

    getOS = platform.system()

    # check if user runs MS Windows

    if platform.system() == "Windows":
        print("Oops! Your OS is not meant to run more, try using WSL, or use Linux! Exiting in 2 seconds.")
        time.sleep(2)
        quit()
    else:
        text_input = input("This is the first setup of the MOTD module/program of Poshy"
                           "\nPlease set up your MOTD: ")
        with open(MSG_PATH, 'w') as msgtxt:
            msgtxt.write(text_input)
else:
    with open(MSG_PATH) as msgtxt:
        readmsg = msgtxt.read()
        print(readmsg)
