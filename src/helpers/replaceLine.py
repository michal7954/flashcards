from helpers.consts import dataFile


def replaceLine(lineNumber, data):
    lines = open(dataFile, 'r', encoding="utf-8").readlines()
    lines[lineNumber] = ';'.join(data) + '\n'
    out = open(dataFile, 'w', encoding="utf-8")
    out.writelines(lines)
    out.close()
