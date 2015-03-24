
class jtkSerial:

    import usbmux
    import SocketServer
    import select
    from optparse import OptionParser
    import sys
    import threading
    import struct

    mux = any
    psock = any
    dispatchFunctionDict = {'setSchedule': setSchedule,
                            'getSchedule': getSchedule,
                            'getTemp': getTemp,
                            'setTemp': setTemp, #used for demo in absence of temp sensor
                            'setDate': setDate,
                            'setSetPoint': setSetPoint}
    def __init__(self):
        print "intialzing Serial Communication"
        

    def scanForDevice(self):
        print "Looking for devices..."
        try:
            self.mux = self.usbmux.USBMux()
        except:
            print "no device"
            return False
        if not self.mux.devices:
            self.mux.process(1.0)
        if not self.mux.devices:
            print "No device found"
            return False
        else:
            print "scan return true"
            return True

    def connectToDevice(self):
        dev = self.mux.devices[0]
        print "connecting to device %s" % str(dev)
        try:
            self.psock = self.mux.connect(dev, 2345)
        except:
            print "connect fail"
            return False
        return True

    def readWriteControl(self, hvac, sched):
        isConnected = True
        while isConnected:
            msg = self.psock.recv(1024)
            try:
                self.psock.send(msg)
            except:
                isConnected = False
            if not msg:
                isConnected = False
            else:
                print msg
                dipatchMessage(msg)

        return isConnected
            
            

    def closeConnection(self):
        psock.close()

    def dispatchMessage(self, msg):
        messageObj = parseMessage(msg)
        
        #each message type maps to a dispatch function 
        dispatchFunctionDict[messageObj.msgType](messageObj)
        
