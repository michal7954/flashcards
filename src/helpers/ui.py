from helpers.consts import wordColor, defaultColor, mistakeColor, correctColor
from os import system
from helpers.timer import getTimer


def printWord(content):
    print(f'{wordColor}{content}{defaultColor}')

def printMistake(content):
    print(f'{mistakeColor}{content}{defaultColor}')

def printCorrect(content):
    print(f'{correctColor}{content}{defaultColor}')

def printHeader():
    system('cls')
    print('Flashcards')
    print('Copyright © 2022 by Michał Madeja')
    print()
    print('Opcje:')
    print('1 - podpowiedź')
    print('2 - wyświetl odpowiedź')
    print('3 - odtwórz słówko')
    print('4 - znajdź słówko w diki.pl')
    print('5 - modyfikuj przed zapisaniem')
    print()

def printSummary(summary):
    print(f'Czas nauki {getTimer()}')
    print(f'Statystyki {summary[0]}-{summary[1]}')

def printFlashcard(cardNumber, cardsNumber, cardProgress, maxLevel, definition):
    print(f'Słówko {cardNumber}/{cardsNumber}')
    print(f'Poziom {cardProgress}/{maxLevel}')
    print()
    printWord(definition)

def printError(specific):
    print(f'Wystąpił problem: {specific}')

def printClosing(summary):
    printHeader()
    printSummary(summary)
    print()
    input('Dzisiaj już nie ma więcej słówek\n[Enter]')