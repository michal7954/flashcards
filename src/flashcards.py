from helpers.replaceLine import replaceLine
from helpers.consts import dataFile, days
from datetime import date
from Flashcard import Flashcard
from helpers.differencesNumber import differencesNumber
from helpers.ui import printFlashcard, printSummary, printHeader, printClosing, printCorrect, printMistake
from sys import exit
from colorama import init as initColorama
from helpers.timer import resetInactivityTimer, stopTimer
from helpers.smartInput import smartInput


def prepareFlashcards():

    try:
        records = open(dataFile, 'r', encoding="utf-8").readlines()
    except FileNotFoundError:
        input('Plik data.txt nie istnieje\n[Enter]')
        exit()
    
    today = date.today()
    flashcards = []

    for lineNumber, record in enumerate(records):
        data = record.rstrip('\n').split(';')

        if len(data) == 1:
            continue

        if not len(data) in [2, 4]:
            input(f'Błędny wiersz w pliku data.txt:\n{record}[Enter]')
            exit()

        try: 
            if len(data) == 2:
                data = data[:2]
                data.extend(['0', str(today)])
                replaceLine(lineNumber, data)

            if data[3] == 'None':
                data[3] = str(today)
                replaceLine(lineNumber, data)
                continue

            data[2] = int(data[2])
            data[3] = date.fromisoformat(data[3])

            if data[2] < len(days) and data[3] <= today:
                flashcards.append(Flashcard(lineNumber, *data))

        except:
            input(f'Błędny wiersz w pliku data.txt:\n{record}[Enter]')
            exit()

    return sorted(flashcards, key=lambda card: card.progress, reverse=True)


def questionFlashcards(flashcards):

    summary = [0, 0]

    for cardNumber, card in enumerate(flashcards, start=1):

        printHeader()
        printSummary(summary)
        printFlashcard(cardNumber, len(flashcards), card.progress, len(days)-1, card.definition)

        hint = 0
        decision = False

        while True:
            operators = ['1', '2', '3', '4']
            print()
            answer = smartInput(operators)
            resetInactivityTimer()

            if answer in operators:
                if answer == '1':
                    hint += 1
                    while hint < len(card.entry) and card.entry[hint] == ' ' :
                        hint +=1
                    printCorrect(card.entry[:hint])
                    if hint == len(card.entry):
                        decision = card.decide()
                        break
                elif answer == '2':
                    printCorrect(f'{card.entry}')
                    decision = card.decide()
                    break
                elif answer == '3':
                    card.read()
                elif answer == '4':
                    card.openInDiki()

            else:
                result = differencesNumber(card.entry, answer)
                if result == 0:
                    printCorrect('Odpowiedź poprawna')
                    decision = card.decide()
                    break
                else:
                    printMistake(f'Różnic: {result}')

        if decision:
            summary[0] += 1
        else:
            summary[1] += 1

    stopTimer()

    return summary


def main():

    initColorama()

    flashcards = prepareFlashcards()

    summary = questionFlashcards(flashcards)

    printClosing(summary)


if __name__ == '__main__':
    main()
