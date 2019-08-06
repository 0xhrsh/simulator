from driver import drive
data=drive()
E=0.7
for x in data:
	if x[0]<1:
		print("Stop")
	elif abs(x[1])-x[2]>E:
		print("right")
	elif x[2]-abs(x[2])>E:
		print("left")
	else:
		print("straight")