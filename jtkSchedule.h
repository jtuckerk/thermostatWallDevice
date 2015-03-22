#ifndef jtkSchedule_h
#define jtkSchedule_h
#include <string>
#include "rtc_clock.h"
#include "Arduino.h"



#define SEGMENTS_PER_HOUR 4
#define SEGMENTS_PER_DAY 24*SEGMENTS_PER_HOUR
#define DAYS 7
class jtkSchedule {

 private:
  void setTime();
  
  struct timeSegment {
    int temp;
      
  };
  struct timeSegment schedule[DAYS][SEGMENTS_PER_DAY]= {{{0}}};
  struct timeSegment defaultTimeSegment = {68};
 public:
  enum days {
    monday=1,
    tuesday=2,
    wednesday=3,
    thursday=4,
    friday=5,
    saturday=6,
    sunday=7
  };

  struct DHM{
    enum days day;
    int hours;
    int minutes;
  };

  RTC_clock rtc_clock(0);
  
  jtkSchedule();
  //updates time on microcontroller and any schedule updates
  void update();

  void setTimeSegment(int TempF, struct DHM time);
  
  int setRange(int TempF, struct DHM timeStart, struct DHM timeEnd);
  
  void getScheduleVal(struct DHM time, int *a, int* b);

  int getTimeSegment(int day, int hourMin);

  std::string getRange(struct DHM start, struct DHM end);
  void getSegmentFromTime(int *a, int *b, struct DHM clock);
  void convertTimeToSegment(int *a, int*b, struct DHM clock);
};
#endif

