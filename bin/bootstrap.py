import os

while True:
    app = input("PyOS: $> ")
    if app == 'exitos':
        exit()
    try:
        eval(app)
    except:
        os.system(app)
