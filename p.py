from PractClass import MyClass
from jtkSchedule import jtkSchedule
from jtkSchedule import segment

sched = jtkSchedule()

sched.printSchedule()
x = MyClass()
print(sched.getTimeSegment([1,5,20,1]))
sched.setTime(10,6,8,20)
sched.getTime()
seg = segment()
seg.tempSetPoint = 70
sched.setSegmentRange([2,0,0,0],[3,0,0,0], 70)


str = sched.getJsonSchedule()
dict = sched.parseJsonSchedule(str)

print sched.scheduleDict['Friday']
print dict['Friday']
