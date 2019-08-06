#f=open("data.csv","w")
from pprint import pprint
from straight import Straight
from turn import turnRight
from turn import turnLeft
import random
#classes for turning: 0: left, 1: Straight, 2: Right
def drive():
	data=[]
	for i in range(100):
		k=random.random()
		if k<0.4:
			data+=Straight(n=1)
		elif k<0.6:
			data+=turnLeft(n=0)
		else:
			data+=turnRight(n=0)
	return data
#f.write(data)
#f.close()