from pprint import pprint
from straight import Straight
from turn import turnRight
from turn import turnLeft
import random
data=[]
for i in range(100):
	k=random.random()
	if k<0.5:
		data+=Straight(n=2)
	elif k<0.75:
		data+=turnLeft(n=2)
	else:
		data+=turnRight(n=2)
pprint(data)