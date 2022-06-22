import readchar
from pyautogui import typewrite

def smartInput(operators):
    key = readchar.readkey()
    if key in operators:
        print(key)
    elif key:
        typewrite(key)
        key = input()
    else:
        key = input()
    return key
