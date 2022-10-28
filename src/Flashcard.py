from datetime import date, timedelta
import webbrowser
import pyttsx3

from helpers.replaceLine import replaceLine
from helpers.consts import days, dikiUri
from helpers.ui import printError
from helpers.timer import resetInactivityTimer
from helpers.smartInput import smartInput


today = date.today()

class Flashcard:
    def __init__(self, line, entry, definition, progress, date) -> None:
        self.line = line
        self.entry = entry.strip()
        self.definition = definition.strip()
        self.progress = progress
        self.date = date
        self.modifyBeforeSaving = False

    def save(self):
        replaceLine(self.line, [self.entry, self.definition, str(self.progress), str(self.date)], self.modifyBeforeSaving)

    def decide(self):
        print()

        decision = None
        while not decision in ['t', 'n']:
            print('Czy zaliczyć? [t/n/3/4/5]: ', end='')
            decision = smartInput(['t', 'n', '1', '2', '3', '4', '5'])
            resetInactivityTimer()
            if decision == '3':
                self.read()
            if decision == '4':
                self.openInDiki()
            if decision == '5':
                self.modifyBeforeSaving = True
                print('Będziesz mógł zmodyfikować linijkę po decyzji.')

        if decision == 't':
            self.progress += 1
        elif decision == 'n':
            self.progress = 0

        if self.progress < len(days):
            self.date = today + timedelta(days=days[self.progress])
        else:
            self.date = today

        self.save()

        return decision == 't'

    def read(self):
        try:
            engine = pyttsx3.init()
            engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
            engine.setProperty('rate', 110)
            engine.say(self.entry.replace('/',' '))
            engine.runAndWait()
        except Exception as e:
            printError(e)

    def openInDiki(self):
        query=self.entry.replace(' ', '+')
        uri = f'{dikiUri}{query}'
        webbrowser.open(uri)