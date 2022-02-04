from helpers.consts import wordColor, defaultColor, mistakeColor, correctColor
from os import system


def printWord(content):
    print(f'{wordColor}{content}{defaultColor}')

def printMistake(content):
    print(f'{mistakeColor}{content}{defaultColor}')

def printCorrect(content):
    print(f'{correctColor}{content}{defaultColor}')

def printHeader():
    system('cls')
    print('Nauka słówek')
    print('© Michał Madeja\n')
    print('Opcje:')
    print('1 - podpowiedź')
    print('2 - wyświetl odpowiedź')
    print()


def printFlashcard(cardNumber, cardsNumber, cardProgress, maxLevel, definition):
    print(f'Słówko: {cardNumber}/{cardsNumber}')
    print(f'Poziom: {cardProgress}/{maxLevel}')
    printWord(definition)


def printFooter():
    system('cls')
    input('Dzisiaj już nie ma więcej słówek\n[Enter]')
