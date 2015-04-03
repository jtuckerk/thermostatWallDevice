from collections import OrderedDict
import sys
import datetime
import time
import json

#@@segment not used - not able to todo Json decode on object within object
class segment:
    def __init__(self):
        self.tempSetPoint = 68
        
    tempSetPoint = 68

class jtkSchedule:

    #each segment holds the temp set point of each for time steps during the day 
    SEGMENTS_PER_HOUR = 4;
    SEGMENTS_PER_DAY = 24*SEGMENTS_PER_HOUR

    #holds the time difference between the device's clock
    #and the actual time as set by the controlling smart phone
    timeOffset = 0    

    #the keys, Monday, Tuesday... map to a SEGMENTS_PER_DAY sized array
    #that holds the the point temperature for the time of day
    scheduleDict = OrderedDict()


    #each segment is initialized to 68 degrees


    daysArray = ["Monday",
                 "Tuesday",
                 "Wednesday",
                 "Thursday",
                 "Friday",
                 "Saturday",
                 "Sunday"]

    #each segment is initialized to 68 degrees and home
    defaultSegment = {'temp': 68, 'status': 'Home'}


    def __init__(self):
        self.scheduleDict.update({'Monday':[]})
        self.scheduleDict.update({'Tuesday':[]})
        self.scheduleDict.update({'Wednesday':[]})
        self.scheduleDict.update({'Thursday':[]})
        self.scheduleDict.update({'Friday':[]})
        self.scheduleDict.update({'Saturday':[]})
        self.scheduleDict.update({'Sunday':[]})

        #loads default setpoint temp
        for day in self.scheduleDict:
            for x in range(0, self.SEGMENTS_PER_DAY):
                self.scheduleDict[day].append(self.defaultSegment)

    #@@debugging print
    def printSchedule(self):
        i=0
        for day in self.scheduleDict:
            print day
            i=0
            for n in self.scheduleDict[day]:
                print str(n) + 'seg:' + str(day)+  ','+ str(i) 
                i+=1

    #sets the offset for the time and day (does not keep track of months/years)
    #from the devices clock - allows the smartphone to control the time
    def setTime(self, day, hour, minute, second):
        offset = time.time()-(day*24*60*60 + hour*60*60 + minute*60 +second)
        self.timeOffset = offset

    #gets time based of offset. days 0-6 24 hour format
    #returns an array 
    def getTime(self):
        sysTime = time.time() - self.timeOffset
        day = int(sysTime/(24*60*60))
        hour = int(sysTime%(24*60*60)/(3600))
        minute = int(sysTime%(24*60*60)%(3600)/60)
        second = int(sysTime%(24*60*60)%(3600)%60)
        day = day%7
        return [day, hour, minute, second]

    #gets segment at a certain time as specified by [day, hour, minute, second]
    def getTimeSegment(self, DHMStuple):
        abTuple = self.getSegmentCoordinates(DHMStuple)
                
        return self.scheduleDict[self.daysArray[abTuple[0]]][abTuple[1]]

    #sets segment at a certain time as specified by [day, hour, minute, second]
    def setTimeSegment(self, DHMStuple, segment):
        abTuple = self.getSegmentCoordinates(DHMStuple)
        self.setSegmentWithABtuple(abTuple, segment)

    #used to set the exact array position of the time
    def setSegmentWithABtuple(self, abTuple, segment):
        self.scheduleDict[self.daysArray[abTuple[0]]][abTuple[1]] = segment

    #sets a range of setpoints     
    def setSegmentRange(self, startDHMS, endDHMS, segment):
        startTuple = self.getSegmentCoordinates(startDHMS)
        endTuple = self.getSegmentCoordinates(endDHMS)
        while(startTuple[0] < endTuple[0]):
            while(startTuple[1] < self.SEGMENTS_PER_DAY):
                self.setSegmentWithABtuple(startTuple, segment)
                print(startTuple)
                startTuple[1]+=1

            startTuple[1]=0
            startTuple[0]+=1
        while(startTuple[1] <= endTuple[1]):
            self.setSegmentWithABtuple(startTuple, segment)
            print(startTuple)
            startTuple[1]+=1
            
        
    #used to get the coordinates of a setpoint in the schedule dictionary's arrays
    def getSegmentCoordinates(self, DHMStuple):
        day = DHMStuple[0]
        hour = DHMStuple[1]
        minute = DHMStuple[2]
        second = DHMStuple[3]
        
        a = day 

        b = hour*self.SEGMENTS_PER_HOUR + int(minute/(60/self.SEGMENTS_PER_HOUR))
        return [a,b]

    #gets temp setpoint for current time
    def getCurrentSeg(self):
        return self.getTimeSegment(self.getTime())

    #gets a json string representation of the schedule for serial communication
    def getJsonSchedule(self):
        return (json.dumps(self.scheduleDict, sort_keys=False))

    #turns a JSON string to a ordered dictionary object representing a schedule
    def parseJsonSchedule(self, JSONstring):
        orderedDict = json.JSONDecoder(object_pairs_hook=OrderedDict).decode(JSONstring)
        return orderedDict

    #take a json string schedule and sets it as the thermostats schedule
    def setScheduleJSON(self, JSONschedule):
        self.scheduleDict = parseJsonSchedule(JSONschedule)
    def setScheduleDict(self, schedDict):
        self.scheduleDict = schedDict
    
