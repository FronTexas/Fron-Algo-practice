def sort(a,high):
	counts = [0] * high 
	
	for number in a: 
		counts[number] += 1 

	a_index = 0
	for i,c in enumerate(counts):
		for j in range(0,c):
			a[a_index] = i
			a_index+= 1 

a = [37,89,41,64,53]
sort(a,100)
print a 
