from helpers.consts import color, defaultColor
from os import system


def printColor(content):
    print(f'{color}{content}{defaultColor}')


def printHeader():
    system('cls')
    print('Nauka słówek\n')
    print('Opcje:')
    print('1 - podpowiedź')
    print('2 - wyświetl odpowiedź')
    print()


def printWord(cardNumber, cardsNumber, cardProgress, maxLevel, definition):
    print(f'Słówko: {cardNumber}/{cardsNumber}')
    print(f'Poziom: {cardProgress}/{maxLevel}')
    printColor(definition)


def printFooter():
    system('cls')
    input('Dzisiaj już nie ma więcej słówek\n[Enter]')
