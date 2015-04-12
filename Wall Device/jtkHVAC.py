from udooPins import udooPins

class jtkHVAC:

    #Conventional HVAC Control switches
    ########################
    # G     - Fan
    # Y     - 1st Stage Cooling
    # Y2    - 2nd Stage Cooling
    # W     - 1st Stage Heating
    # W2/E  - 2nd Stage Heating
    # W3/O/B- 3rd Stage Heating
    currentSegment = {'setPoint': 68, 'status': 'Home'}
    temp = 68
    HVACstatus = "Off"
    pins = udooPins()
    def getTemp(self):
         #@@ either add console temp input or get thermometer
        #print "Temp is " +str(self.temp)+ "F"
        return self.temp

    def setTemp(self, temp):
        self.temp = temp
    #@@need to make a set setpoint method to do a temporary range    
    def setSetPoint(self, currentSegment):
        self.currentSegment['setPoint'] = currentSegment['setPoint']
        self.currentSegment['status'] = currentSegment['status']

    def getSetPoint(self):
        return self.currentSegment['setPoint']

    def getHVACstatus(self):
        return self.HVACstatus

    def controlUpdate(self, sched):
        temp = self.getTemp()
        self.pins.allOff()
        #sets the setpoint to the current setpoint in the schedule
        self.setSetPoint(sched.getCurrentSeg());
        #cooling
        if(temp > self.currentSegment['setPoint'] + .3): # + .3 avoids frequent switching
            self.HVACstatus = "Cooling"
            #low cool Y and G on
            if(temp <= self.currentSegment['setPoint'] +2):
                print("low cool G and Y on")
                self.pins.On(self.pins.fan)
                self.pins.On(self.pins.Y)
            #high cool
            else:
                print("high cool G, Y and Y2 on")
                self.pins.On(self.pins.fan)
                self.pins.On(self.pins.Y)
                self.pins.On(self.pins.Y2)
                

        #heating
        elif(temp < self.currentSegment['setPoint'] -.3): # + .3 avoids frequent switching
            self.HVACstatus = "Heating"            
            #low heat G and W
            if(temp >= self.currentSegment['setPoint'] -2):
                print("low heat G and W on")
                self.pins.On(self.pins.fan)
                self.pins.On(self.pins.W)

            #medium heat
            elif(temp >= self.currentSegment['setPoint'] -4 and temp < self.currentSegment['setPoint'] -2):
                print("Medium heat G, W and W2 on")
                self.pins.On(self.pins.fan)
                self.pins.On(self.pins.W)
                self.pins.On(self.pins.W2)
            #high heat
            else:
                print("High heat G, W, W2 and W3 on")
                self.pins.On(self.pins.fan)
                self.pins.On(self.pins.W)
                self.pins.On(self.pins.W2)
                self.pins.On(self.pins.W3)

        else:
            self.HVACstatus = "Off"            
            print "chillin"
