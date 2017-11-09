def isLuckySpotAvailable(parkingLot,luckySpot):
	xtl,ytl = luckySpot[0],luckySpot[1]
	xbr,ybr = luckySpot[2],luckySpot[3]

	for i in range(xtl,xbr + 1):
		for j in range(ytl,ybr + 1):
			if parkingLot[i][j] == 1:
				return False
	return True

def parkingSpot(carDimensions, parkingLot, luckySpot):
	if not isLuckySpotAvailable(parkingLot,luckySpot): 
		return False 

	xtl,ytl = luckySpot[0],luckySpot[1]
	xbr,ybr = luckySpot[2],luckySpot[3]
	l,w = carDimensions
	if xbr - xtl + 1 == w and ybr - ytl + 1 == l:
		possible_from_left = True
		possible_from_right = True

		for i in range(xtl,xtl + w):
			for j in range(0,ytl + 1):
				if parkingLot[i][j] == 1:
					possible_from_left = False
					break
			if(not possible_from_left): break 

		for i in range(xtl,xtl + w):
			for j in range(ybr,len(parkingLot[i])):
				if parkingLot[i][j] == 1:
					possible_from_right = False
					break
			if(not possible_from_right): break 
		return possible_from_left or possible_from_right
	else: 
		possible_from_top = True 
		possible_from_bottom = True 
		
		for i in range(0,xtl):
			for j in range(ytl,ytl + w):
				if parkingLot[i][j] == 1:
					possible_from_top = False
					break
			if(not possible_from_top): break 

		for i in range(xbr,len(parkingLot)):
			for j in range(ytl,ytl + w):
				if parkingLot[i][j] == 1:
					possible_from_bottom = False
					break
			if(not possible_from_bottom): break 
		return possible_from_top or possible_from_bottom



parkingLot = [[1, 0, 0, 0, 1, 0],
              [1, 0, 0, 0, 1, 0],
              [0, 1, 0, 0, 0, 0],
              [1, 0, 1, 0, 1, 1]]
luckySpot = [0, 2, 2, 3] 
carDimensions = [3,2]

print parkingSpot(carDimensions,parkingLot,luckySpot)
# print isLuckySpotAvailable(parkingLot,luckySpot)