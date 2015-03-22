from PractClass import MyClass
from jtkSchedule import jtkSchedule

sched = jtkSchedule()

sched.printSchedule()
x = MyClass()

sched.setTime(10,6,8,20)
sched.getTime()
print(sched.scheduleDict.items()[0][0])
