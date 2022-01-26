from helpers.replaceLine import replaceLine
from helpers.consts import dataFile, days
from datetime import date
from Flashcard import Flashcard
from helpers.differencesNumber import differencesNumber
from helpers.ui import printFlashcard, printHeader, printFooter, printCorrect, printMistake
from sys import exit


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

        if not len(data) in [2, 4]:
            input(f'Błędny wiersz w pliku data.txt:\n{record}\n[Enter]')
            exit()

        if len(data) == 2:
            data = data[:2]
            data.extend(['0', str(today)])
            replaceLine(lineNumber, data)

        if data[3] == 'None':
            continue

        data[2] = int(data[2])
        data[3] = date.fromisoformat(data[3])

        if data[3] <= today:
            flashcards.append(Flashcard(lineNumber, *data))

    return sorted(flashcards, key=lambda card: card.progress, reverse=True)


def questionFlashcards(flashcards):

    for cardNumber, card in enumerate(flashcards, start=1):

        printHeader()
        printFlashcard(cardNumber, len(flashcards), card.progress, len(days)-1, card.definition)

        hint = 0
        while True:
            answer = input('\n')

            if answer.isnumeric():
                if answer == '1':
                    hint += 1
                    printCorrect(card.entry[:hint])
                    if hint == len(card.entry):
                        card.decide()
                        break
                elif answer == '2':
                    printCorrect(f'{card.entry}')
                    card.decide()
                    break

            else:
                result = differencesNumber(card.entry, answer)
                if result == 0:
                    printCorrect('Odpowiedź poprawna')
                    card.decide()
                    break
                else:
                    printMistake(f'Różnic: {result}')


def main():

    flashcards = prepareFlashcards()

    questionFlashcards(flashcards)

    printFooter()


if __name__ == '__main__':
    main()
