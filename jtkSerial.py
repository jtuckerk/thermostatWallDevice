
class jtkSerial:

    import usbmux
    import SocketServer
    import select
    from optparse import OptionParser
    import sys
    import threading
    import struct
    #import RPi.GPIO as GPIO

    mux = 0
    psock = 0
    
    def __init__(self):
        print "intialzing Serial Communication"
        mux = usbmux.USBMux()

    def scanForDevice():
        print "Waiting for devices..."
        if not mux.devices:
            mux.process(1.0)
        if not mux.devices:
            print "No device found"
            return false
        else:
            return true

    def connectToDevice(self):
        dev = mux.devices[0]
        print "connecting to device %s" % str(dev)
        psock = mux.connect(dev, 2345)

    def read():
        while True:
            msg = psock.recv(1024)
            print msg
            if not msg: break

        print "finished reading"
            
            

    def closeConnection():
        psock.close()
        
