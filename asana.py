import datetime
sacred_date_time = datetime.date(2015,1,1)

DAY = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
DAY_TO_NUM = DAY = {"Monday" : 0,"Tuesday" : 1,"Wednesday" : 2,"Thursday" : 3,"Friday" : 4,"Saturday" : 5,"Sunday" : 6}

def getProperDateStr(n):
	if(n % 10 == n):
		return "0" + str(n)
	return str(n)

def recurringTask(firstDate, k, daysOfTheWeek, n):
	firstDate = firstDate.split('/')
	year = int(firstDate[2])
	month = int(firstDate[1])
	day = int(firstDate[0])
	today_date_time = datetime.date(year,month,day)

	delta = (today_date_time - sacred_date_time).days
	today_day_of_week = (3 + delta) % 7
	daysOfTheWeek = [DAY_TO_NUM[e] for e in daysOfTheWeek]
	daysOfTheWeek = set(daysOfTheWeek)
	tr = []
	counter = 0
	day = today_day_of_week

	while len(tr) < len(daysOfTheWeek):
		day = day%7
		if day in daysOfTheWeek:
			tr.append(counter)
		day += 1
		counter += 1

	look_back = 0 
	week_window = 0 
	prev = tr[look_back]

	while(len(tr) < n):
		if week_window == 0:
			tr.append(tr[look_back] + (k*7))
		else:
			tr.append(tr[-1] + tr[look_back] - prev)
		prev = tr[look_back]
		week_window += 1
		look_back += 1

	for i,t in enumerate(tr):
		t_date_time = today_date_time + datetime.timedelta(days=t)
		day = getProperDateStr(t_date_time.day)
		month = getProperDateStr(t_date_time.month)
		year = getProperDateStr(t_date_time.year)
		tr[i] = day + "/" + month + "/" + year
	return tr
print recurringTask("01/01/2015",2,["Monday","Thursday"],4)










	


