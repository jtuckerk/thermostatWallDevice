/* -*- C++ -*- */
#include "jtkSerialCommunication.h"
#include "jtkSchedule.h"
#include "jtkHVAC.h"


jtkSerial androidCom;
jtkHVAC homeHVAC;
jtkSchedule homeSchedule;

void setup() {
  //initialize communications
  //androidCom.initialize();
  Serial.begin(9600);
//initialize clock


  

}
void loop() {
  
 struct jtkSchedule::DHM start, end;
 start.day = jtkSchedule::monday;
  start.hour = 0;
  start.minutes = 0;

  end.day = jtkSchedule::tuesday;
  end.hour = 0;
  end.minutes = 0;
   delay(1000);

   
   Serial.print(homeSchedule.getTimeSlice(2, 10));  
   //homeSchedule.getRange(start, end) ;


}























