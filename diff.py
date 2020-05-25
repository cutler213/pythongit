from functools import *

nums=[1,2,3,4,5,6,7]
le=len(nums)

eve=reduce(lambda a,b:a+b,nums)/le


print(eve)