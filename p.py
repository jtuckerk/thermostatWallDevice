from PractClass import MyClass
from jtkSchedule import jtkSchedule
from jtkSchedule import segment
from jtkHVAC import jtkHVAC 
from collections import OrderedDict
import json
from json import JSONEncoder
# sched = jtkSchedule()

# sched.printSchedule()
# x = MyClass()
# print(sched.getTimeSegment([1,5,20,1]))
# sched.setTime(10,6,8,20)
# sched.getTime()
# seg = segment()
# seg.tempSetPoint = 70
# sched.setSegmentRange([2,0,0,0],[3,0,0,0], 70)


# str = sched.getJsonSchedule()
# dict = sched.parseJsonSchedule(str)

# print sched.scheduleDict['Friday']
# print dict['Friday']

#hvac = jtkHVAC()

#hvac.setSetPoint(50)

# for n in range(50, 80):
#     hvac.setSetPoint(n)
#     hvac.controlUpdate()

def a():
    print 'A'

def b():
    print 'B'

    ##@@syntax for ordered dict assignment
dict1 =OrderedDict([('apple', 6), ('banana', 3), ('asshole', 5), ('orange', 2), ('pear', 1)])

class random:
    temp = 5

a = random()

#str = json.dumps(a, sort_keys=False)

object1 = {'type1':'sched', 'obj': 4}

msg =  json.dumps(object1, sort_keys=False)

orderedDictObj2 = json.JSONDecoder(object_pairs_hook=OrderedDict).decode(msg)

#print jsonStrObj1
#obj2 = json.loads(jsonStrObj1)
print orderedDictObj2['obj']
#print orderedDictObj2[0]


#print str

