from helpers.replaceLine import replaceLine
from datetime import date, timedelta
from helpers.consts import days, dikiUri
from helpers.ui import printError
today = date.today()
import webbrowser
import pyttsx3
from helpers.timer import resetInactivityTimer


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
            decision = input('Czy zaliczyć? [t/n/3/4]: ')
            resetInactivityTimer()
            if decision == '3':
                self.read()
            if decision == '4':
                self.openInDiki()

        if decision == 't':
            self.progress += 1
        elif decision == 'n':
            self.progress = 0

        if self.progress < len(days):
            self.date = today + timedelta(days=days[self.progress])
        else:
            self.date = None

        self.save()

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