# This file provides a serial interface using JSON message objects to recieve update
# commands and respond to information queries from the controlling IOS device

import json
from json import JSONDecoder    
import select
class jtkSerial:

    import usbmux
    import SocketServer

    from optparse import OptionParser
    import sys
    import threading
    import struct
    import Queue
    from collections import OrderedDict

    from jtkHVAC import jtkHVAC
    from jtkSchedule import jtkSchedule

    #references to device Schedule and HVAC control
    hvac = any
    sched = any

    #communication interfaces
    mux = any
    psock = any

    #buffers for unread or unsent messages - keeps separate messages separate
    outGoingMsgQueue = Queue.Queue()
    incomingMsgQueue = Queue.Queue()
    
    def __init__(self):
        print "intialzing Serial Communication"

        #holds mapping of message types to a function to handle said message type
        self.dispatchFunctionDict = {'setSchedule': self.setSchedule,
                                     'getSchedule': self.getSchedule,
                                     'getTemp': self.getTemp,
                                     'setTemp': self.setTemp, #used for demo in absence of temp sensor
                                     'setDate': self.setDate,
                                     'setSetPoint': self.setSetPoint,
                                     'getHVACstatus':self.getHVACstatus,
                                     'setTime':self.setTime}

        #maps a response type for outgoing messages in response to incoming
        #currently all the same for simplicity
        self.replyDict = {'setSchedule': 'setSchedule',
                          'getSchedule': 'getSchedule',
                          'getTemp': 'getTemp',
                          'setTemp': 'setTemp',
                          'setDate': 'setDate',
                          'setSetPoint': 'setSetPoint',
                          'getHVACstatus': 'getHVACstatus'}

    #scans for a device Signature corresponding to an IOS device 
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

    # Once IOS device is found attempt to connect - this requires the user
    # to trust the wall device running this software
    def connectToDevice(self):
        dev = self.mux.devices[0]
        print "connecting to device %s" % str(dev)
        try:
            self.psock = self.mux.connect(dev, 2345)
        except:
            print "connect fail"
            return False
        return True

    # loop that reads and writes while the Wall device and IOS device are connected
    def readWriteControl(self, hvac, sched):
        self.hvac = hvac
        self.sched = sched
        
        isConnected = True
        counter = 0
        while isConnected:
            #sets connection timeout
            ready = select.select([self.psock], [], [], 1)

            if ready[0]:
                #Receives incoming 30000 bytes
                msg = self.psock.recv(30000)
            
                if not msg:
                    isConnected = False

                else:
                    #print msg #@@ debug

                    #Multiple messages may be received as a single string:
                    # "{Message1}{Message}" need to be split before they
                    # can be parsed by the JSON parser. once split they are
                    # placed on the incoming message queue
                    self.splitMessages(msg)

                    # Reads and handles all pending messages
                    while(not self.incomingMsgQueue.empty()):
                        self.dispatchMessage(self.incomingMsgQueue.get())
            try:
                # Send off all messages created as responses to incoming
                # messages
                if(not self.outGoingMsgQueue.empty()):
                    print "sending message"
                    outMsg = self.outGoingMsgQueue.get()
                    self.psock.send(outMsg)
                    #print "SENT!:" + outMsg #@@ debug
            except Exception, e:
                print "sendFail: " + str(e)
                isConnected = False

            #updates HVAC controls every time the read times out
            self.hvac.controlUpdate(sched)

        return isConnected

    # parses {Message1}{message2}...{messageN} and places them
    # as separate messages on incoming queue
    def splitMessages(self, msg):
        count = 0
        start = 0
        end = 0

        #looks for balanced curly braces
        for c in msg:
            if c == '{':
                count+=1
            if c == '}':
                count-=1
            end+=1
            if count == 0:
                #push string
                print "pushing: " + msg[start:end]
                self.incomingMsgQueue.put(msg[start:end])
                start = end
                
    def closeConnection(self):
        psock.close()

    #from the message type specified in each JSON object sent this function
    # determines the appropriate function to be called to handle the request
    def dispatchMessage(self, msg):

        msgObj =  json.JSONDecoder(object_pairs_hook=self.OrderedDict).decode(msg)

        #each message type maps to a dispatch function 
        if type(msgObj) is self.OrderedDict:
            #checks if the msgObj has a field 'type' or the type in that field
            # maps to any defined function
            if self.dispatchFunctionDict.get(msgObj.get('type', None), None):
                self.dispatchFunctionDict[msgObj['type']](msgObj)
            else:
                print "improperly formatted message object"
        else:
            print "unknown message: " + msg

    #sets device time from smartphone time
    def setTime(self,msgObj):
        print 'setTime'
        self.sched.setTime(msgObj['time'])

    # sets entire schedule from sent schedule object
    def setSchedule(self, msgObj):
        print "setSchedule"
        self.sched.setScheduleDict(msgObj['schedule'])
        #self.sched.printSchedule() #@@debug print
        
    #gets current schedule upon request to be sent on the serial bus
    def getSchedule(self, msgObj):
        print "getSchedule"

        res = self.constructReplyJson(msgObj['type'], self.sched.scheduleDict)
        self.outGoingMsgQueue.put(res)
    
    #gets the current temperature to be sent on the serial bus
    def getTemp(self, msgObj):
        print "getTemp"
        temp = self.hvac.getTemp()
        res = self.constructReplyJson(msgObj['type'], temp)
        self.outGoingMsgQueue.put(res)

    #used for Demo purposes - the user can set the home temp in the absence
    #of a real thermometer
    def setTemp(self, msgObj):
        print "setTemp"
        self.hvac.setTemp(msgObj['temp'])

    #sets the Wall device date equal to the IOS device date 
    def setDate(self, msgObj):
        print "setDate"
        dtDHMS = msgObj['datetime']
        self.sched.setTime(dtDHMS[0], dtDHMS[1], dtDHMS[2], dtDHMS[3])

    # for a single time segment - sets the set point
    def setSetPoint(self, msgObj):
        print "setSetPoint"
        setPoint = msgObj['setPoint']
        self.hvac.setSetPoint(setPoint)
        self.sched.setTimeSegment(self.sched.getTime(), setPoint)

    # gives the IOS device info on whether the HVAC is heating cooling or off
    def getHVACstatus(self, msgObj):
        print "getsetPoint"
        stat = self.hvac.getHVACstatus()
        res = self.constructReplyJson(msgObj['type'], stat)
        self.outGoingMsgQueue.put(res)
        
    #constructs a json string reply
    #takes the request object whose 'type' is used to find the proper
    #return 'type', and the object is added to the appropriate object field
    def constructReplyJson(self, reqType, resJson):
        respType = self.replyDict[reqType]

        response = {'type':respType, 'obj': resJson}
        return json.dumps(response, sort_keys=False)
