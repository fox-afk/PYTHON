import sys
import random
from pyfiglet import figlet

if len(sys.argv)==1:
    isRandomFont= True
elif len(sys.argv) ==3 and (sys.argv[1]=="-f"or  sys.argv=="--font"):
    isRandomFont=False
else:
    print("invalid usage")
    sys.exit(1)




figlet.getFonts()


if isRandomFont== False:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        print("invalid message")
        sys.exit(1)
else:
    font=random.choice(figlet.getFonts())

msg= input("input: ")
print("output: ")
print(figlet.renderText(msg)) 