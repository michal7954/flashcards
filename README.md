# Flashcards

Flashcards is an everyday tool designed to help users learn and retain vocabulary through a structured repetition system. The application is built primarily with Python and includes features that facilitate efficient learning and review of vocabulary.

## Key Use Cases

- **Vocabulary Review:** Users can review vocabulary words at regular intervals to enhance retention.
- **Progress Tracking:** The application tracks user progress and provides visual feedback on learning status.
- **Customizable Decks:** Users can create and manage custom decks of vocabulary cards tailored to their learning needs.
- **Scheduled Repetitions:** The system schedules repetitions based on user performance to optimize learning efficiency.
- **Deck Automanagement:** The order of querying vocabulary is determined by an algorithm that maximizes efficiency even during short learning sessions.
- **Extra features:** Play the word or serch it in an online dictionary.

![obraz](https://github.com/user-attachments/assets/4701a298-d062-455d-9122-c7422c30c4dc)

## Code Highlights

### Vocabulary Review Logic - [flashcards.py](https://github.com/michal7954/flashcards/blob/e098722c2dc3879d274ae6521686932b3ea21678/src/flashcards.py#L70-L113)
```python
for cardNumber, card in enumerate(flashcards, start=1):

    printHeader()
    printSummary(summary)
    printFlashcard(cardNumber, len(flashcards), card.progress, len(days)-1, card.definition)

    hint = 0
    decision = False

    while True:
        operators = ['1', '2', '3', '4', '5']
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
            elif answer == '5':
                print('Będziesz mógł zmodyfikować linijkę po decyzji.')
                card.modifyBeforeSaving = True

        else:
            result = differencesNumber(card.entry, answer)
            if result == 0:
                printCorrect('Odpowiedź poprawna')
                decision = card.decide()
                break
            else:
                printMistake(f'Różnic: {result}')
```

### Determining next revision date of particular word - [Flashcard.py](https://github.com/michal7954/flashcards/blob/e098722c2dc3879d274ae6521686932b3ea21678/src/Flashcard.py#L42-L50)
```python
if decision == 't':
    self.progress += 1
elif decision == 'n':
    self.progress = 0

if self.progress < len(days):
    self.date = today + timedelta(days=days[self.progress])
else:
    self.date = today
```
