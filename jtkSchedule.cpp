#include "jtkSchedule.h"

jtkSchedule::jtkSchedule(){
  for(int i = 0; i< DAYS; i++){
    for(int j = 0; j < SEGMENTS_PER_DAY; j++){
      schedule[i][j] = defaultTimeSegment;
    }
  }
}

void jtkSchedule::setTime(struct DHM time){

  
}
//updates time on microcontroller and any schedule updates
void jtkSchedule::update(){
  
}
void jtkSchedule::setTimeSegment(int TempF, struct DHM time)
{
  int a,b;
  getScheduleVal(time, &a, &b); 
  schedule[a][b].temp = TempF;
}

int jtkSchedule::setRange(int TempF, struct DHM timeStart, struct DHM timeEnd){
  int a,b;
  int c,d;
  getScheduleVal(timeStart, &a, &b);
  getScheduleVal(timeEnd, &c, &d);

  if (a>c ||  (a==c && b>d))
    return -1;
  else{
    for(a; a<=c; a++)
      for(b; b<=d; b++)
	schedule[a][b].temp = TempF;
      
  }
}
void jtkSchedule::getScheduleVal(struct DHM time, int* a, int* b){
  *a = time.day;
  *b = time.hours*SEGMENTS_PER_HOUR + time.minutes/(60/SEGMENTS_PER_HOUR);
}

int jtkSchedule::getTimeSegment(int day, int hourMin){    
  return schedule[day][hourMin].temp;
}

void getSegmentFromTime(int *a, int *b, RTC_clock clock){
  convertTimeToSegment(a,b,clock);
  
}

void convertTimeToSegment(int *a, int*b, RTC_clock clock){
  clock.get_hours();
  clock.get_minutes();
  
}
std::string jtkSchedule::getRange(struct DHM start, struct DHM end){
  int a,b;
  int c,d;
  getScheduleVal(start, &a, &b);
  getScheduleVal(end, &c, &d);
  Serial.print("[");
  for(a; a<=c; a++){
    for(b; b<=d; b++){
      Serial.print(schedule[a][b].temp);
      if (a!=c && b!=d)
	Serial.print(", ");
    }
    Serial.print("\n");
  }
  return "";
}





