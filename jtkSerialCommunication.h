#ifndef jtkSerial_h
#define jtkSerial_h

#include "Arduino.h"
#include "serial.h"

class jtkSerial{

 public:
  jtkSerial(){
    this.initialize();
  }
  initialize(){
    Serial.begin(115200);
  }
  run(){
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
#endif
