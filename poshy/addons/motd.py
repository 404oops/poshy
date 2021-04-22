import os

MSG_PATH = os.path.join(os.path.dirname(__file__), ".motd")

if not os.path.exists(MSG_PATH):
    text_input = input("This is the first setup of the MOTD module/program of Poshy"
                       "\nPlease set up your MOTD: ")
    with open(MSG_PATH, 'w') as msgtxt:
        msgtxt.write(text_input)
else:
    with open(MSG_PATH) as msgtxt:
        readmsg = msgtxt.read()
        print(readmsg)
