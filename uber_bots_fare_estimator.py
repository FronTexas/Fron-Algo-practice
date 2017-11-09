def fareEstimator(ride_time, ride_distance, cost_per_minute, cost_per_mile):
    toReturn = [0] * len(cost_per_mile)
    for i in range(0,len(cost_per_mile)):
        toReturn[i] += ride_time * cost_per_minute[i]
        toReturn[i] += ride_distance * cost_per_mile[i]
    return toReturn
