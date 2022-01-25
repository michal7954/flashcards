from helpers.consts import dataFile


def replaceLine(lineNumber, data):
    lines = open(dataFile, 'r').readlines()
    lines[lineNumber] = ';'.join(data) + '\n'
    out = open(dataFile, 'w')
    out.writelines(lines)
    out.close()
