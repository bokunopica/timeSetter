import os
import random
import time
import ntplib


def timeSync():
    c = ntplib.NTPClient()
    response = c.request('pool.ntp.org')
    syncDateTime = response.tx_time
    syncDate = time.strftime('%Y-%m-%d', time.localtime(syncDateTime))
    syncTime = time.strftime('%X', time.localtime(syncDateTime))
    os.system('date {} && time {}'.format(syncDate, syncTime))


def timeSwift(sleepingTime=2):
    datetimeNow = time.time()
    dateNow = time.strftime('%Y-%m-%d', time.localtime(datetimeNow))
    timeNow = time.strftime('%X', time.localtime(datetimeNow))
    traceBackSec = random.randint(3, 6) * 31536000
    datetimePast = datetimeNow - traceBackSec
    datePast = time.strftime('%Y-%m-%d', time.localtime(datetimePast))
    timePast = time.strftime('%X', time.localtime(datetimePast))
    os.system('date {} && time {}'.format(datePast, timePast))
    time.sleep(sleepingTime)
    os.system('date {} && time {}'.format(dateNow, timeNow))
