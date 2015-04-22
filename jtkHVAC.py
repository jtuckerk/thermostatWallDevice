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
         #controled by setTemp command sent by IOS device for demo purposes
        #print "Temp is " +str(self.temp)+ "F"
        return self.temp

    ## used for demo purposes - normally the temp stored in self.temp
    # would be from the temperature sensor
    def setTemp(self, temp):
        self.temp = temp

    #updates a segment which consists of a setPoint for the temperature
    # and a status - home or away - implemented like this to provide
    # an option to update the implementation later
    def setSetPoint(self, currentSegment):
        self.currentSegment['setPoint'] = currentSegment['setPoint']
        self.currentSegment['status'] = currentSegment['status']

    # returns current home set point 
    def getSetPoint(self):
        return self.currentSegment['setPoint']

    # returns 'heating', 'cooling' or 'off' depending on HVAC status 
    def getHVACstatus(self):
        return self.HVACstatus

    # based off the temperature of the home and the setpoint, the
    # state of the switches of the HVAC are set accordingly
    def controlUpdate(self, sched):
        temp = self.getTemp()
        self.pins.allOff()
        #sets the setpoint to the current setpoint in the schedule
        self.setSetPoint(sched.getCurrentSeg());

         # used to keep the HVAC from rapidly switching on and off when
         # temp is fluctuating about the set point
        tempChangeBuffer = .5
        
        #cooling
        if(temp > self.currentSegment['setPoint'] + tempChangeBuffer): # + buffer avoids frequent switching
            self.HVACstatus = "Cooling"
            #low cool Y and G on
            if(temp <= self.currentSegment['setPoint'] +2):
                #print("low cool G and Y on")
                self.pins.On(self.pins.fan)
                self.pins.On(self.pins.Y)
            #high cool
            else:
                #print("high cool G, Y and Y2 on")
                self.pins.On(self.pins.fan)
                self.pins.On(self.pins.Y)
                self.pins.On(self.pins.Y2)
                

        #heating
        elif(temp < self.currentSegment['setPoint'] - tempChangeBuffer): # + bufferavoids frequent switching
            self.HVACstatus = "Heating"            
            #low heat G and W
            if(temp >= self.currentSegment['setPoint'] -2):
                #print("low heat G and W on")
                self.pins.On(self.pins.fan)
                self.pins.On(self.pins.W)

            #medium heat
            elif(temp >= self.currentSegment['setPoint'] -4 and temp < self.currentSegment['setPoint'] -2):
                #print("Medium heat G, W and W2 on")
                self.pins.On(self.pins.fan)
                self.pins.On(self.pins.W)
                self.pins.On(self.pins.W2)
            #high heat
            else:
                #print("High heat G, W, W2 and W3 on")
                self.pins.On(self.pins.fan)
                self.pins.On(self.pins.W)
                self.pins.On(self.pins.W2)
                self.pins.On(self.pins.W3)

        else:
            self.HVACstatus = "Off"            

