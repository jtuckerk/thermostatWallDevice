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

    fan = open(fanValue, 'w')
    Y = open(YValue, 'w')
    Y2 = open(Y2Value, 'w')
    W = open(WValue, 'w')
    W2 = open(W2Value, 'w')
    W3 = open(W3Value, 'w')
    
    allSwitches = [fan, Y, Y2, W, W2, W3]

    def __init__(self):
        dirArray = [ open(self.fanDir, 'w'),
                     open(self.YDir, 'w'),
                     open(self.Y2Dir, 'w'),
                     open(self.WDir, 'w'),
                    open(self.W2Dir, 'w'),
                    open(self.W3Dir, 'w')]
        
        for direction in dirArray:
            direction.write('out')
            direction.flush()

    def On(self,pinfile):
        pinfile.write('1')
        pinfile.flush()
        
    def Off(self, pinfile):
        pinfile.write('0')
        pinfile.flush()

    def allOff(self):
        for switch in self.allSwitches:
            self.Off(switch)
