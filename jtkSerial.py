    
class jtkSerial:

    import usbmux
    import SocketServer
    import select
    from optparse import OptionParser
    import sys
    import threading
    import struct
    import queue
    from collections import OrderedDict
    import json
    from json import JSONDecoder

    from jtkHVAC import jtkHVAC
    from jtkSchedule import jtkSchedule


    hvac = any
    sched = any
    
    mux = any
    psock = any
    outGoingMsgQueue = queue()
    
    def __init__(self):
        print "intialzing Serial Communication"
        self.dispatchFunctionDict = {'setSchedule': self.setSchedule,
                                'getSchedule': self.getSchedule,
                                'getTemp': self.getTemp,
                                'setTemp': self.setTemp, #used for demo in absence of temp sensor
                                'setDate': self.setDate,
                                'setSetPoint': self.setSetPoint}
        
        self.replyDict = {'setSchedule': 'setSchedule',
                          'getSchedule': 'getSchedule',
                          'getTemp': 'getTemp'
                          'setTemp': 'setTemp',
                          'setDate': 'setDate',
                          'setSetPoint': 'setSetPoint'}

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
        self.hvac = hvac
        self.sched = sched
        
        isConnected = True
        while isConnected:
            msg = self.psock.recv(1024)
            try:
                if(not outGoingMsgQueue.empty()):
                    outMsg = outGoingMsgQueue.get()
                    self.psock.send(outMsg)
                    print outMsg #@@ debug
            except:
                isConnected = False
            if not msg:
                isConnected = False
            else:
                print msg
                self.dispatchMessage(msg)

        return isConnected
            
            

    def closeConnection(self):
        psock.close()

    def dispatchMessage(self, msg):

        msgObj =  self.json.JSONDecoder(object_pairs_hook=self.OrderedDict).decode(msg)
        msgObj = {'type': 'getSchedule'} #@@debug 
        #each message type maps to a dispatch function 
        if type(msgObj) is dict:
            #checks if the msgObj has a field 'type' or the type in that field
            # matches any defined function
            if self.dispatchFunctionDict.get(msgObj.get('type', None), None):
                self.dispatchFunctionDict[msgObj['type']](msgObj)
            else:
                print "improperly formatted dictionary object"
        else:
            print "unknown message: " + msg

    def setSchedule(self, msgObj):
        print "setSchedule"
        self.hvac.setScheduleDict(msgObj['schedule'])
        self.hvac.printSchedule() #@@debug print
        
    def getSchedule(self, msgObj):
        print "getSchedule"
        jsonStr = self.hvac.getJsonSchedule()
        res = constructReplyJson(msgObj['type'], jsonStr)
        outGoingMsgQueue.put(res)
        
    def getTemp(self, msgObj):
        print "getTemp"

    def setTemp(self, msgObj):
        print "setTemp"

    def setDate(self, msgObj):
        print "setDate"

    def setSetPoint(self, msgObj):
        print "setSetPoint"

    #constructs a json string reply
    #takes the request object whose 'type' is used to find the proper
    #return 'type', and the object is added to the appropriate object field
    def constructReplyJson(self, reqType, resJson):
        respType = replyDict[reqType]
        #@@resObj is already parsed json 
        response = {'type':respType, 'obj': resObj}
        return json.dumps(response, sort_keys=False)
