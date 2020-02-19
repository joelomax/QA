def getdivrange(range1, mult1, mult2):
	for i in range1:
		if i % mult1 == 0 and i % mult2 == 0:
			print(i, end = ",")
ask=0
while ask == 0:
	try:
		userRange = int(input("enter range")
		userIn = int(input("enter 1st number to find multiples: "))
		userIn2 = int(input("enter 2nd number to multiples: "))
		ask=1
	except:
		print("you have entered the wrong input!")

getdivrange(userRange, userIn, userIn2)