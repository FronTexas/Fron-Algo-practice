import sys
def isValid(i,j,matrix):
	return 0 <= i and i < len(matrix) and 0 <= j and j < len(matrix[i]) and matrix[i][j] != 'X'

def hash(kings_positions):
	return str(sorted(kings_positions))

def solve_recursive(matrix,kings_positions,isBobTurn,counter,configuration_visited):
	print 'state = ' + str((isBobTurn,hash(kings_positions)))
	# if((isBobTurn,hash(kings_positions)) in configuration_visited): 
		# counter[0] += configuration_visited[(isBobTurn,hash(kings_positions))]
		# return
	moved = False
	for k,kings_position in enumerate(kings_positions):
		i,j = kings_position
		if isValid(i-1,j,matrix): 
			moved = True 
			kings_positions[k] = (i-1,j)
			solve_recursive(matrix,kings_positions,not isBobTurn,counter,configuration_visited)
			kings_positions[k] = (i,j)
		
		if isValid(i-1,j-1,matrix): 
			moved = True 
			kings_positions[k] = (i-1,j-1)
			solve_recursive(matrix,kings_positions,not isBobTurn,counter,configuration_visited)
			kings_positions[k] = (i,j)

		if isValid(i,j-1,matrix): 
			moved = True 
			kings_positions[k] = (i,j-1)
			solve_recursive(matrix,kings_positions,not isBobTurn,counter,configuration_visited)
			kings_positions[k] = (i,j)
	if not isBobTurn and not moved: 
		print 'BOB WINS'
		counter[0] += 1
	configuration_visited[(isBobTurn,hash(kings_positions))] = counter[0]

def buildKingsPositions(matrix):
	kings_positions = []
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if matrix[i][j] != 'K': continue 
			kings_positions.append((i,j)) 
	return kings_positions

def solve(matrix):
	counter = [0]
	kings_positions = buildKingsPositions(matrix)
	configuration_visited = {}
	solve_recursive(matrix,kings_positions,True,counter,configuration_visited)
	print configuration_visited
	if(counter[0] > 0):
		print 'WIN ' + str(counter[0])
	else:
		print 'LOSE'

if __name__ == "__main__":
    q = int(raw_input().strip())
    for a0 in xrange(q):
        n = int(raw_input().strip())
        board = []
        board_i = 0
        for board_i in xrange(n):
            board_t = list(str(raw_input().strip()))
            board.append(board_t)
        solve(board)

