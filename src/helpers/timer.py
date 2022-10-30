from datetime import datetime, timedelta
import threading

from helpers.consts import maxInactivityTime


timer = datetime(1, 1, 1, 0, 0, 0)
inactivityTime = 0
stopped = False
active = True


def resetInactivityTimer():
    global inactivityTime, active
    inactivityTime = 0
    active = True


def getTimer():
    global timer
    return f'{timer.minute}:{timer.strftime("%S")}'


def incrementTimer():
    global inactivityTime, timer, active
    inactivityTime += 1
    if inactivityTime <= maxInactivityTime:
        timer += timedelta(0, 1)
    else:
        if active:
            active = False
            print("Zatrzymano odliczanie czasu\n")


def stopTimer():
    global stopped
    stopped = True


def setTimer(func, sec):
    def func_wrapper():
        if stopped:
            return None
        setTimer(func, sec)
        func()

    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


setTimer(incrementTimer, 1)
