from jtkSerial import jtkSerial
from jtkSchedule import jtkSchedule
from jtkHVAC import jtkHVAC

hvac = jtkHVAC()
serial = jtkSerial()
sched = jtkSchedule()

connected = False

def connected():
    while connected:
        serial.read()
    
def notConnected():
    while(not connected):
        connected = serial.scanForDevice()

    
    
