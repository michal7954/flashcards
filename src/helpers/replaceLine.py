from pynput.keyboard import Controller

from helpers.consts import dataFile


keyboard = Controller()

def replaceLine(lineNumber, data, modifyBeforeSaving = False):
    lines = open(dataFile, 'r', encoding="utf-8").readlines()
    orginalLine = ';'.join(data)

    line = ''
    if modifyBeforeSaving:
        while not lineCorrect(line):
            keyboard.type(orginalLine)
            line = input()
    else:
        line = orginalLine

    lines[lineNumber] = line + '\n'
    out = open(dataFile, 'w', encoding="utf-8")
    out.writelines(lines)
    out.close()

def lineCorrect(line):
    data = line.rstrip('\n').split(';')
    return len(data) == 4