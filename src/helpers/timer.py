from time import sleep
from datetime import datetime, timedelta
from helpers.consts import maxInactivityTime
import threading

timer = datetime(1, 1, 1, 0, 0, 0)
inactivityTime = 0


def resetInactivityTimer():
    global inactivityTime
    inactivityTime = 0

def getTimer():
    global timer
    return f'{timer.minute}:{timer.strftime("%S")}'

def incrementTimer():
    global inactivityTime, timer
    inactivityTime+=1
    if inactivityTime <= maxInactivityTime:
        timer+=timedelta(0, 1)


def setTimer(func, sec):
    def func_wrapper():
        setTimer(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

setTimer(incrementTimer, 1)
