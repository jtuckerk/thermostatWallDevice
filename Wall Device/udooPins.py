#!/usr/local/bin/python

import time 

class udooPins:

#Conventional HVAC Control switches pin mappings
    ########################
    # G     - Fan
    fanPath = '/sys/class/gpio/gpio1'
    fanDir = fanPath + '/direction'
    fanValue = fanPath + '/value'
    # Y     - 1st Stage Cooling
    YPath = '/sys/class/gpio/gpio19'
    YDir = YPath + '/direction'
    YValue = YPath + '/value'
    # Y2    - 2nd Stage Cooling
    Y2Path = '/sys/class/gpio/gpio21'
    Y2Dir = Y2Path + '/direction'
    Y2Value = Y2Path + '/value'
    # W     - 1st Stage Heating
    WPath = '/sys/class/gpio/gpio9'
    WDir = WPath + '/direction'
    WValue = WPath + '/value'
    # W2/E  - 2nd Stage Heating
    W2Path = '/sys/class/gpio/gpio3'
    W2Dir = W2Path + '/direction'
    W2Value = W2Path + '/value'
    # W3/O/B- 3rd Stage Heating
    W3Path = '/sys/class/gpio/gpio40'
    W3Dir = W3Path + '/direction'
    W3Value = W3Path + '/value'

    fan = None
    Y = None
    Y2 = None
    W = None
    W2 = None
    W3 = None
    
    def __init__(self):


        try:
            self.fan = open(self.fanValue, 'w')
            self.Y = open(self.YValue, 'w')
            self.Y2 = open(self.Y2Value, 'w')
            self.W = open(self.WValue, 'w')
            self.W2 = open(self.W2Value, 'w')
            self.W3 = open(self.W3Value, 'w')
            
            dirArray = [ open(self.fanDir, 'w'),
                         open(self.YDir, 'w'),
                         open(self.Y2Dir, 'w'),
                         open(self.WDir, 'w'),
                         open(self.W2Dir, 'w'),
                         open(self.W3Dir, 'w')]
        
            for direction in dirArray:
                direction.write('out')
                direction.flush()
        except Exception as e:
            print e
            connected = False
            print "not connected to udoo pins"
        self.allSwitches = [self.fan, self.Y, self.Y2, self.W, self.W2, self.W3]

        self.connected = True
            
                
    def On(self,pinfile):
        if connected:
            
            pinfile.write('1')
            pinfile.flush()
        
    def Off(self, pinfile):
        if connected:
            pinfile.write('0')
            pinfile.flush()

    def allOff(self):
        if connected:
            for switch in self.allSwitches:
                self.Off(switch)
