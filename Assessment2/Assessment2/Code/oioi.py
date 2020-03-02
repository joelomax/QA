import random
def f():
    rl = []
    c= 0
	while c < 5:
		r = random.randint(100,200)
		if r % 2 == 0:
			rl.append(r)
			c+=1
		else:
			r=random.randint(100,200)
	return rl
print(five())