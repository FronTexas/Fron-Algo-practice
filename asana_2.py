import datetime
a = datetime.date(2015,1,1)

DAY = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
DAY_TO_NUM = DAY = {"Monday" : 0,"Tuesday" : 1,"Wednesday" : 2,"Thursday" : 3,"Friday" : 4,"Saturday" : 5,"Sunday" : 6}
MAX = 2**32

def recurringTask(firstDate, k, daysOfTheWeek, n):
	toReturn = []
	firstDate = firstDate.split('/')
	year = int(firstDate[2])
	month = int(firstDate[1])
	day = int(firstDate[0])
	b = datetime(year,month,day)
	delta = ((b-a).days) % 7 
	
	first_day = (day + delta) % 7
	daysOfTheWeek = [DAY_TO_NUM[e] for e in daysOfTheWeek]
	daysOfTheWeek = sorted(daysOfTheWeek)


	max_of_days_week = max(daysOfTheWeek)
	if max_of_days_week == first_day:
		first_task_day = daysOfTheWeek[-1]
		first_task_day_index = len(daysOfTheWeek) - 1
	elif max_of_days_week > first_day:
		first_task_day = MAX;
		first_task_day_index = 0
		for i,day in enumerate(daysOfTheWeek): 
			if(first_day < day):
				first_task_day = day
				first_task_day_index = i
				break
	else: 
		first_task_day = daysOfTheWeek[0]
		first_task_day_index = 0
	
	prev = first_day
	i = first_task_day_index
	while(len(toReturn) < len(daysOfTheWeek)):
		if (i == len(daysOfTheWeek)):
			i = i % len(daysOfTheWeek)
		current = daysOfTheWeek[i]
		diff = current - prev 
		if diff < 0:
			x = prev
			adder = 0
			while(current - (x % 7) != 0):
				x+=1 
				adder += 1 
			diff = adder 

		if(len(toReturn) == 0):
			toReturn.append(diff)
		else: 
			toReturn.append(toReturn[-1] + diff)
		prev = current
		i+=1

	count = 0
	i = 0
	while(len(toReturn) < n):
		while(count < len(daysOfTheWeek)):
			current = toReturn[i]
			if count == 0
				toReturn.append(current + (k * 7))
			else:
				toReturn.append(toReturn[-1] + (current - prev))
			count += 1
			i+=1
			prev = current
		count = 0

	
	print toReturn








	


