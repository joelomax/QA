def one(input):
	s = ""
	for char in input:
		s += char * 3
	return s
print(one("hello"))