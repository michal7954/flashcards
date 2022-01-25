from helpers.replaceLine import replaceLine
from datetime import date, timedelta
from helpers.consts import days
today = date.today()


class Flashcard:
    def __init__(self, line, entry, definition, progress, date) -> None:
        self.line = line
        self.entry = entry
        self.definition = definition
        self.progress = progress
        self.date = date

    def save(self):
        replaceLine(self.line, [self.entry, self.definition, str(self.progress), str(self.date)])

    def decide(self):
        print()

        decision = None
        while not decision in ['t', 'n']:
            decision = input('Czy zaliczyć? [t/n]: ')

        if decision == 't':
            self.progress += 1
        elif decision == 'n':
            self.progress = 0

        if self.progress < len(days):
            self.date = today + timedelta(days=days[self.progress])
        else:
            self.date = None

        self.save()
