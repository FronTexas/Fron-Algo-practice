n = 27 
companies = []
for _n in range(n):
	line = raw_input().split(' ')
	dash = line[0]
	check1 = line[1]
	check2 = line[2]
	check = check1 + ' ' + check2
	company_name = line[3]
	booth = line[4]
	companies.append((company_name,booth))

print '-------------'
companies.sort(key=lambda x: x[1])
for i,company in enumerate(companies): 
	print ''.join([e + ' ' for e in company])
