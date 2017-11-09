with open('bos_input.py') as f:
	rows = f.readlines()

n = int(rows[0])
grid = [[int(num) for num in row.split(' ')] for row in rows[1:]]

# initialize maximum_final to 0 
maximum_final = 0 
for row in range(len(grid)):
	for col in range(len(grid[row])):
		# go right
		adder = 0 
		total_right = 1
		if col + 3 < len(grid[row]):
			while col + adder < len(grid[row]) and adder < 4:
				total_right *= grid[row][col + adder]
				adder += 1

		# go vertical
		adder = 0
		total_vertical = 1 
		if row + 3 < len(grid):
			while row + adder < len(grid) and adder < 4:
				total_vertical *= grid[row + adder][col]
				adder += 1

		# go diagonal_righ
		adder = 0 
		total_diagonal_right = 1
		if col + 3 < len(grid[row]) and row + 3 < len(grid):
			while row + adder < len(grid) and col + adder < len(grid[row]) and adder < 4:
				total_diagonal_right *= grid[row + adder][col + adder]
				adder += 1

		# go diagonal_left
		adder = 0 
		total_diagonal_left = 1 
		if col - 3 >= 0 and row  + 3 < len(grid):
			while row + adder >= 0 and col - adder >= 0 and adder < 4: 
				total_diagonal_left *= grid[row + adder][col - adder]
				adder += 1 
		maximum_final = max(maximum_final, total_right, total_vertical, total_diagonal_right, total_diagonal_left)
print 'The greatest product is ' + str(maximum_final)