def maxDuffleBagValue(cakeTuples,maxWeight):
	maxValueForiPoundsBag = [0] * (maxWeight + 1)

	for bagMaxWeight in range(0,maxWeight + 1):
		maxSoFar = 0 								
		for cakeTuple in cakeTuples: 
			currentMax = 0 
			weight,value  = cakeTuple
			if bagMaxWeight - weight >= 0: 
				currentMax += value 
				currentMax += maxValueForiPoundsBag[bagMaxWeight - weight]
				maxSoFar = max(maxSoFar,currentMax)
		maxValueForiPoundsBag[bagMaxWeight] = maxSoFar
	return maxValueForiPoundsBag[-1]

print maxDuffleBagValue([(7,160),(3,90),(2,15)],7)

	