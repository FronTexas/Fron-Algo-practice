def findUniqueDroneId(a):
	multiplications = 1 

	for e in a : 
		multiplications *= e 

	for e in a : 
		if multiplications % (e*e) != 0:
			return e
	return None

print findUniqueDroneId([2,4,4])