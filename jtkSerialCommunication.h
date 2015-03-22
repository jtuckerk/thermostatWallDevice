#ifndef jtkSerial_h
#define jtkSerial_h

#include "Arduino.h"

class jtkSerial{

 public:
  jtkSerial(){
    this->initialize();
  }
  void initialize(){
    Serial.begin(115200);
  }
  void run(){
    int counter =0;
  while(1){
    Serial.print("Tick #");
    Serial.print(counter++, DEC);
    Serial.print("\n");

    if (Serial.peek() != -1) {
      Serial.print("Read: ");
      do {
	Serial.print((char) Serial.read());
      } while (Serial.peek() != -1);
      Serial.print("\n");
    }
    delay(1000);
  }
  }
  
};
#endif
