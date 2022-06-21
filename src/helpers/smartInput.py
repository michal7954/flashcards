import readchar
from pyautogui import typewrite

def smartInput(operators):
    key = readchar.readkey()
    if key in operators:
        print(key)
    else:
        typewrite(key)
        key = input()
    return key
