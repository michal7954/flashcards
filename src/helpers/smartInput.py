import readchar
from pynput.keyboard import Key, Controller

keyboard = Controller()

def smartInput(operators):
    key = readchar.readkey()
    if key == '\033[A':
        keyboard.press(Key.up)
        key = input()
    elif key in operators:
        print(key)
    elif key:
        keyboard.type(key)
        key = input()
    else:
        key = input()
    return key
