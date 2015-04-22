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

#runs while not connected
#continues to update HVAC control based on exisiting schedule
def notConnected(found):
    global isConnected
    #runs until a device is found - still updates HVAC
    while(not found):
        #keeps thermostat running on schedule while offline
        offlineRun();
        found = serial.scanForDevice()
        time.sleep(.2)

    #runs once device is found, but before connected
    while(not isConnected):
        offlineRun();
        isConnected = serial.connectToDevice()
        time.sleep(.2)
    print "connected"

#runs while connected  - breaks out if disconnected
def connected():
    global isConnected
    while isConnected:
        print "reading"
        isConnected = serial.readWriteControl(hvac, sched)

#program run loop
while 1:
    if(isConnected):
        #print "connected"
        connected()
    else:
        notConnected(found)
    
    
