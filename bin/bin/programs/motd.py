import os

if os.stat("bin/programs/msg.txt").st_size == 0:
    text_input = input("This is the first setup of the MOTD module/program of Poshy"
                       "\nPlease set up your MOTD: ")
    msgtxt = open("bin/programs/msg.txt", 'r+')
    msgtxt.write(text_input)
else:
    msgtxt = open("bin/programs/msg.txt", 'r+')
    readmsg = msgtxt.read()
    print(readmsg)
