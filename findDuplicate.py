def findDuplicate(theList):
	floor = 1 
	ceiling = len(theList) + 1 

	while floor < ceiling: 
		middlePoint = floor + ((ceiling-floor)/2)			
		lowerFloor,lowerCeiling = floor,middlePoint
		higherFloor,higherCeiling = middlePoint,ceiling

		itemCount = 0
		for item in theList: 
			if lowerFloor <= item <= lowerCeiling:
				itemCount += 1 

		numberOfUniqueElmenets = (lowerCeiling - lowerFloor) + 1

		if itemCount > numberOfUniqueElmenets: 
			ceiling = lowerCeiling
		else:
			floor = higherFloor
			ceiling = higherFloor
	return floor			

