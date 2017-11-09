def merge_ranges(schedules):
	schedules = sorted(schedules, key = lambda x : x[0])

	if len(schedules) == 1: 
		return schedules
	toReturn = []
	lowest = schedules[0][0]
	highest = schedules[0][1]

	sub_schedules = schedules[1:]
	for i,schedule in enumerate(sub_schedules):
		new_low = schedule[0]
		new_high = schedule[1]

		if new_low > highest:
			toReturn.append((lowest,highest))
			lowest = new_low
		highest = max(highest,new_high)

	toReturn.append((lowest,highest))
	return toReturn

print merge_ranges(  [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
print merge_ranges(  [(1, 2), (2, 3)])
print merge_ranges(  [(1, 5), (2, 3)])
print merge_ranges(  [(1, 10), (2, 6), (3, 5), (7, 9)])