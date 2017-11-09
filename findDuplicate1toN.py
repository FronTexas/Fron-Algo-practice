def findDuplicate1toN(a):
	n = len(a) - 1 
	theSum = int(n*(n+1)/2)
	arraySum = 0 
	for e in a:
		arraySum += e
	return arraySum - theSum

a = [i for i in range(1,101)]
a.append(69)

print findDuplicate1toN(a)

