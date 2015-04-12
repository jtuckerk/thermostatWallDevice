#!/usr/bin/env python

from jtkSerial import jtkSerial
from jtkSchedule import jtkSchedule
from jtkHVAC import jtkHVAC
import time 

isConnected = False
found = False

hvac = jtkHVAC()
serial = jtkSerial()
sched = jtkSchedule()

def offlineRun():    
    hvac.controlUpdate(sched)

def notConnected(found):
    global isConnected
    while(not found):
        #keeps thermostat running on schedule while offline
        offlineRun();
        found = serial.scanForDevice()
        #time.sleep(.5)

    while(not isConnected):
        offlineRun();
        isConnected = serial.connectToDevice()
        #time.sleep(.5)
    print "connected"

def connected():
    global isConnected
    while isConnected:
        print "reading"
        isConnected = serial.readWriteControl(hvac, sched)

while 1:
    if(isConnected):
        print "connected"
        connected()
    else:
        notConnected(found)
    
    
