def find_seperator(s):
	i = 0 
	while s[i].isalpha():
		i+=1
	return s[i]

def find_index_of_year_month_date(a):
	year_index = 0 
	month_index = 0 
	date_index = 0 

	for i in range(len(a)):
		if a[i] == 'yyyy' or a[i] == 'yyyy\n':
			year_index = i 
		elif a[i] == 'mm' or a[i] == 'mm\n':
			month_index = i 
		elif a[i] == 'dd' or a[i] == 'dd\n':
			date_index = i 

	return year_index,month_index,date_index

def print_year_month_date(year,month,date):
	print 'year = ' + year 
	print 'month = ' + month
	print 'date = ' + date

def buildAnswer(year,month,date,a):
	answer = []
	for i in range(len(a)):
		if a[i] == 'yyyy':
			answer.append(year)
		elif a[i] == 'mm':
			answer.append(month)
		elif a[i] == 'dd':
			answer.append(date)
	return answer

with open('./microsoft_challenge_input.txt') as f:
	for line in f:
		line = line.rstrip()
		line_splitted = line.split(' ')
		current_date,current_format,desired_format = line_splitted

		seperator = find_seperator(current_format)

		current_format_splitted = current_format.split(seperator)
		
		year_index,month_index,date_index = find_index_of_year_month_date(current_format_splitted)

		current_date_splitted = current_date.split(seperator)
		year,month,date = current_date_splitted[year_index],current_date_splitted[month_index],current_date_splitted[date_index]


		desired_seperator = find_seperator(desired_format)

		desired_format_splitted = desired_format.split(desired_seperator)
		
		answer = buildAnswer(year,month,date,desired_format_splitted)

		final_answer = ''
		for i in range(len(answer)):
			final_answer += str(answer[i])
			if i < len(answer) - 1:
				final_answer += desired_seperator
		print final_answer


