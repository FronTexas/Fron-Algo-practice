def fareEstimator(ride_time, ride_distance, cost_per_minute, cost_per_mile):
    toReturn = [0] * len(cost_per_mile)
    for i in range(0,len(cost_per_mile)):
        toReturn[i] += ride_time * cost_per_minute[i]
        toReturn[i] += ride_distance * cost_per_mile[i]
    return toReturn

import math

def perfectCityHelper(min_distance,dis_so_far,pos,destination,visited):
	current_x,current_y = pos
	visited.add((current_x,current_y))
	xdest,ydest = destination
	
	if (current_x,ydest) == destination:
		min_distance[0] = min(min_distance[0],dis_so_far + math.fabs(ydest-current_y))
		return
	if (xdest,current_y) == destination:
		min_distance[0] = min(min_distance[0],dis_so_far + math.fabs(xdest-current_x))
		return
	if (current_x,current_y) == destination:
		min_distance[0]  = min(min_distance[0],dis_so_far)
		return
	
	is_x_integer = (float(current_x)).is_integer()
	is_y_integer = (float(current_y)).is_integer()

	if(is_x_integer and is_y_integer):
		perfectCityHelper(min_distance, dis_so_far + math.fabs(ydest - current_y),(current_x,ydest),destination,visited)
		perfectCityHelper(min_distance, dis_so_far + math.fabs(xdest - current_x),(xdest,current_y),destination,visited)
	elif(is_x_integer):
		next_y = math.ceil(current_y)
		perfectCityHelper(min_distance, dis_so_far + math.fabs(next_y - current_y),(current_x,next_y),destination,visited)
		
		next_y = math.floor(current_y)
		perfectCityHelper(min_distance,dis_so_far + math.fabs(next_y - current_y),(current_x,next_y),destination,visited)
	elif(is_y_integer):
		next_x = math.ceil(current_x)		
		perfectCityHelper(min_distance, dis_so_far + math.fabs(next_x - current_x), (next_x,current_y),destination,visited)

		next_x = math.floor(current_x)		
		perfectCityHelper(min_distance,dis_so_far + math.fabs(next_x - current_x),(next_x,current_y),destination,visited)



def perfectCity(departure,destination):
	min_distance = [2**32]
	dis_so_far = 0
	perfectCityHelper(min_distance,dis_so_far,(departure[0],departure[1]),(destination[0],destination[1]),set([]))
	return min_distance[0]

print perfectCity((0.4,1),(0.9,3))
print perfectCity((0,0.9),(1,2.9))
print perfectCity((0,0.2),(7,0.5))







