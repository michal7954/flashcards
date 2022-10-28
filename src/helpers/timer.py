from datetime import datetime, timedelta
import threading

from helpers.consts import maxInactivityTime


timer = datetime(1, 1, 1, 0, 0, 0)
inactivityTime = 0
stopped = False


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
