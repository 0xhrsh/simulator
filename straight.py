import random
def Straight(cardim=5,wid=9,error=0.25,n=3):
	wid=(wid-cardim)/2
	cardim/=2
	dist=[]
	for i in range(10**n):
		ldist=-wid+error*random.random() -error*random.random()-cardim
		rdist=wid+cardim+error*random.random()-error*random.random()
		dist.append([int(10*random.random()),ldist,rdist])
	return dist
from pprint import pprint
#pprint(Straight())