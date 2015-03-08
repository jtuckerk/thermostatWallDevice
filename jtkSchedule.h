#ifndef jtkSchedule_h
#define jtkSchedule_h

#include "Arduino.h"

#define SLICES_PER_DAY 24*4
#define DAYS 7
class jtkSchedule{

 public:

  void update();

 private:
  void setTime();

  timeSlice schedule[DAYS][SLICES_PER_DAY];
  
  struct schedule {
    
  }
  
  struct timeSlice {
    int temp;
    
  }
};
#endif
