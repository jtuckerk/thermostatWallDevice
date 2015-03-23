
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
    
    def __init__(self):
        print "intialzing Serial Communication"
        self.mux = self.usbmux.USBMux()

    def scanForDevice(self):
        print "Waiting for devices..."
        if not self.mux.devices:
            self.mux.process(1.0)
        if not self.mux.devices:
            print "No device found"
            return False
        else:
            return True

    def connectToDevice(self):
        dev = self.mux.devices[0]
        print "connecting to device %s" % str(dev)
        try:
            self.psock = self.mux.connect(dev, 2345)
        except:
            return False
        return True

    def read(self):
        while True:
            msg = self.psock.recv(1024)
            print msg
            if not msg: break

        return False
            
            

    def closeConnection(self):
        psock.close()
        
