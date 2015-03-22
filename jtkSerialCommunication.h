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
  void go(){
  }
};
#endif
















































