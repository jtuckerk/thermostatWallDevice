from collections import OrderedDict
import sys
import datetime
import time

class segment:
    tempSetPoint = 68

class jtkSchedule:

    SEGMENTS_PER_HOUR = 4;
    SEGMENTS_PER_DAY = 24*SEGMENTS_PER_HOUR
    timeOffset = 0    
    array = [1,2,3,4]
    scheduleDict = OrderedDict()

    defaultSegment = segment()

    def __init__(self):
        self.scheduleDict.update({'Monday':[]})
        self.scheduleDict.update({'Tuesday':[]})
        self.scheduleDict.update({'Wednesday':[]})
        self.scheduleDict.update({'Thursday':[]})
        self.scheduleDict.update({'Friday':[]})
        self.scheduleDict.update({'Saturday':[]})
        self.scheduleDict.update({'Sunday':[]})
        for day in self.scheduleDict:
            for x in range(0, self.SEGMENTS_PER_DAY):
                self.scheduleDict[day].append(self.defaultSegment)
    
    def printSchedule(self):
        for day in self.scheduleDict:
            print day
            for n in self.scheduleDict[day]:
                    print n.tempSetPoint
    
    def setTime(self, day, hour, minute, second):
        offset = time.time()-(day*24*60*60 + hour*60*60 + minute*60 +second)
        self.timeOffset = offset

        
    def getTime(self):
        sysTime = time.time() - self.timeOffset
        day = sysTime/(24*60*60)
        hour = sysTime%(24*60*60)/(3600)
        minute = sysTime%(24*60*60)%(3600)/60
        second = sysTime%(24*60*60)%(3600)%60
        day = day%7
        return (day, hour, minute, second)
                    
    def getTimeSegmentInfo(self, DHMStuple):
        

        print self.scheduleDict[day]

    def setTimeSegmentInfo(self, DHMStuple, segment):
        k
        

    def getSegmentCoordinates(self, DHMStuple):
        day = DHMStuple[0]
        hour = DHMStuple[1]
        minute = DHMStuple[2]
        second = DHMStuple[3]
        
        a = day 
        b = hour*SE
        return (day, hour*

        
