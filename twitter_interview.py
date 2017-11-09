def printResult(year,months,iterator):
	for i in range(iterator[0],iterator[1],iterator[2]):
		if not months[i]: continue
		toPrint = str(year) + "-"
		if len(months[i]) != 0: 
			toPrint += "0" + str(i) if i%10 == i else str(i)
			toPrint += ", "
			interactionCount = 0
			interactions = [interaction for interaction in months[i]]
			interactions = sorted(interactions)
			for interaction in interactions:
				count = months[i][interaction]
				if count > 0:
					toPrint += interaction + ", " + str(count)
				if interactionCount != len(months[i]) - 1: 
					toPrint += ", "
				interactionCount += 1
		print toPrint

intervals = raw_input().split(', ')
first = intervals[0].split('-')
second = intervals[1].split('-')

first_year = first[0]
second_year = second[0]

first_month = int(first[1])
second_month = int(second[1])

if first_year != second_year:
	bucket = {first_year:[None]*13,second_year:[None]*13}
else:
	bucket = {first_year:[None]*13}
raw_input()
line = raw_input()
while(line):
	date , interaction , count = line.split(', ')
	count = int(count)
	year , month , date = date.split('-')

	if not bucket[year][int(month)]:
		bucket[year][int(month)] = {}

	if interaction in bucket[year][int(month)]:
		bucket[year][int(month)][interaction] += count
	else: 
		bucket[year][int(month)][interaction] = count
	try:
		line = raw_input()
	except (EOFError):
		break

if first_year != second_year:
	printResult(second_year,bucket[second_year],(second_month-1,0,-1))
printResult(first_year,bucket[first_year],(12,first_month-1,-1))

