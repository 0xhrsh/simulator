from math import sqrt
import random
def turnRight(cardim=5,wid=9,v=60,error=0.15,n=3):
	wid=(wid-cardim)/2
	cardim/=2
	dt=1/180
	v=60
	r=8
	w=v/r
	dq=w*dt
	dist=[]
	for i in range(10**n):
		lwid=wid+error*random.random()-error*random.random() +cardim
		rwid=wid+error*random.random()-error*random.random() +cardim
		ldist=-lwid+r*(2*dq)
		rdist=rwid+r*2*dq
		dist.append([ldist,rdist])
	return dist
def turnLeft(cardim=5,wid=9,v=60,error=0.1,n=3):
	wid=(wid-cardim)/2
	cardim/=2
	dt=1/180
	v=60
	r=8
	w=v/r
	dq=w*dt
	dist=[]
	for i in range(10**n):
		lwid=wid+error*random.random()-error*random.random() +cardim
		rwid=wid+error*random.random()-error*random.random() +cardim
		ldist=-lwid-r*(2*dq)
		rdist=rwid-r*2*dq
		dist.append([ldist,rdist])
	return dist