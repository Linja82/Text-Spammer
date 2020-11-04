"""
Spam Typer V1.0

Feed it a text document and it'll type it out with a variable delay between messages.
@author Linja
@date Nov 3, 2020 9:07 PM

Notes:
    To kill the program while it's running, hold down F2
"""

import time
import keyboard

print("Welcome to Spam Typer v1.0\n")
waitTime = float(input("Enter the delay between messages in seconds: "))
hellFile = open(input("Enter the path to the text file: "))

time.sleep(2)

for x in hellFile:
    if keyboard.is_pressed("F2"):
        break
    # print(x)
    keyboard.write(x)
    time.sleep(waitTime)

hellFile.close()
