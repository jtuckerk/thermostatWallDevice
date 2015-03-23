
class jtkHVAC:

    #Conventional HVAC Control switches
    ########################
    # G     - Fan
    # Y     - 1st Stage Cooling
    # Y2    - 2nd Stage Cooling
    # W     - 1st Stage Heating
    # W2/E  - 2nd Stage Heating
    # W3/O/B- 3rd Stage Heating
    setPoint = 68
        
    def getTemp(self):
        temp =68 #@@ either add console temp input or get thermometer
        print "Temp is " +str( temp)+ "F"
        return temp
    
    def setSetPoint(self, setpoint):
        self.setPoint = setpoint
        
    def controlUpdate(self):
        temp = self.getTemp()

        #cooling
        if(temp > self.setPoint + .3): # + .3 avoids frequent switching 
            #low cool Y and G on
            if(temp <= self.setPoint+2):
                print("low cool G and Y on")
            #high cool
            else:
                print("high cool G, Y and Y2 on")

        #heating
        if(temp < self.setPoint -.3): # + .3 avoids frequent switching
            #low heat G and W
            if(temp >= self.setPoint -2):
                print("low heat G and W on")
            #medium heat
            elif(temp >= self.setPoint -4 and temp < self.setPoint -2):
                print("low heat G, W and W2 on")
            #high heat
            else:
                print("low heat G, W, W2 and W3 on")
