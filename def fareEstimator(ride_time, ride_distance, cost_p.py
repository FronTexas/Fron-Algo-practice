def fareEstimator(ride_time, ride_distance, cost_per_minute, cost_per_mile):
    toReturn = [0] * len(cost_per_mile)
    for i in range(0,len(cost_per_mile)):
        toReturn[i] += ride_time * cost_per_minute[i]
        toReturn[i] += ride_distance * cost_per_mile[i]
    return toReturn

import math

def perfectCityHelper(xdp,ydp,xds,yds):
	destination = xds,yds
	distance = 0

	if((xds,ydp) == destination):
		distance += math.fabs(xds-xdp)
		return distance

	distance += math.fabs(int(round(xds)) - xdp)
	current_pos = (int(round(xds)),ydp)

	distance += math.fabs(yds - current_pos[1])
	current_pos = (current_pos[0],yds)

	if current_pos == destination: 
		return distance 

	distance += math.fabs(xds - current_pos[0])
	return distance 

def perfectCity(departure, destination):
	xdp,ydp = departure 
	xds,yds = destination 

	if((ydp).is_integer()):
		return perfectCityHelper(xdp,ydp,xds,yds)
	else: 
		return perfectCityHelper(ydp,xdp,yds,xds)

perfectCity((0.4,1),(0.9,3))

