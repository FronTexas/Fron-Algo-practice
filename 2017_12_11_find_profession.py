'''
	https://codefights.com/interview-practice/task/FwAR7koSB3uYYsqDp
'''

def findProfession(level, pos):
	start = 0 
	end = 2**(level - 1) - 1

	# convert to zero based index because that's the right way to index
	level -= 1 
	pos -= 1
	current_parent = 'Engineer'
	while start < end: 
		mid = (start + end) / 2
		
		# go right
		if mid < pos: 
			if current_parent == 'Engineer': 
				current_parent = 'Doctor'
			elif current_parent == 'Doctor': 
				current_parent = 'Engineer'
			start = mid + 1 
		else: 
			# go left
			end = mid
	return current_parent
