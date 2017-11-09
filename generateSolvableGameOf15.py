from random import randint
def isSolvable(a):
	inversion_count = 0 
	for i,pi in enumerate(a):
		for j in range(i,len(a)):
			pj = a[j]
			if pi > pj: 
				inversion_count += 1
	return inversion_count % 2 == 0

def generate10SolvableGameOf15():
	toReturn = {}

	while(len(toReturn) != 10):
		the15 = []
		numbers = [i for i in range(1,16)]
		
		while (len(numbers)>0):
			randomIndex = randint(0,len(numbers)-1)
			the15.append(numbers[randomIndex])
			del numbers[randomIndex]

		theKey = ''.join(str(e) for e in the15)

		if theKey not in toReturn and isSolvable(the15):
			toReturn[theKey] = the15


	return [toReturn[key] for key in toReturn]

print generate10SolvableGameOf15()