from jtkSerial import jtkSerial
from jtkSchedule import jtkSchedule
from jtkHVAC import jtkHVAC
import time 

isConnected = False
found = False

hvac = jtkHVAC()
serial = jtkSerial()
sched = jtkSchedule()
    
def notConnected(found):
    global isConnected
    while(not found):
        found = serial.scanForDevice()
    while(not isConnected):
        
        isConnected = serial.connectToDevice()
        time.sleep(.5)
    print "connected"

def connected():
    global isConnected
    while isConnected:
       isConnected = serial.read()

while 1:
    if(isConnected):
        print "connected"
        connected()
    else:
        notConnected(found)
    
    
