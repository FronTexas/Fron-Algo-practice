import sys
def isValid(i,j,matrix):
	return 0 <= i and i < len(matrix) and 0 <= j and j < len(matrix[i]) and matrix[i][j] != 'X'

def hash(kings_positions):
	return str(sorted(kings_positions))

def solve_recursive(matrix,kings_positions,isBobTurn,counter,configuration_visited,level):
	print 'state = ' + str((isBobTurn,hash(kings_positions)))
	moved = False
	if level == 0: 
		print kings_positions
	for k,kings_position in enumerate(kings_positions):
		i,j = kings_position
		if isValid(i-1,j,matrix): 
			moved = True 
			kings_positions[k] = (i-1,j)
			if(solve_recursive(matrix,kings_positions,not isBobTurn,counter,configuration_visited,level+1)):
				kings_positions[k] = (i,j)
				if level == 0: 
					print 'culprit 1'
					print '(i,j) :' + str((i,j))
					print 'moved to :' + str((i-1,j-1))
					counter[0] += 1
				else:
					return True
			kings_positions[k] = (i,j)
		
		if isValid(i-1,j-1,matrix): 
			moved = True 
			kings_positions[k] = (i-1,j-1)
			if(solve_recursive(matrix,kings_positions,not isBobTurn,counter,configuration_visited,level+1)):
				kings_positions[k] = (i,j)
				if level == 0: 
					print 'culprit 2'
					print '(i,j) :' + str((i,j))
					print 'moved to :' + str((i-1,j-1))

					counter[0] += 1
				else:
					return True
			kings_positions[k] = (i,j)

		if isValid(i,j-1,matrix): 
			if (i,j) == (1,1):
				moved = True 
			kings_positions[k] = (i,j-1)
			if(solve_recursive(matrix,kings_positions,not isBobTurn,counter,configuration_visited,level + 1)):
				kings_positions[k] = (i,j)
				if level == 0: 
					print 'culprit 3'
					print '(i,j) :' + str((i,j))
					print 'moved to :' + str((i,j-1))
					counter[0] += 1
				else:
					return True
			kings_positions[k] = (i,j)
			
	if not isBobTurn and not moved: 
		print 'BOB WINS'
		return True
	if isBobTurn and not moved: 
		print 'ALICE WINS'
	return False
def buildKingsPositions(matrix):
	kings_positions = []
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if matrix[i][j] != 'K': continue 
			kings_positions.append((i,j)) 
	return kings_positions

def solve(matrix):
	counter = [0]
	kings_positions = sorted(buildKingsPositions(matrix))
	configuration_visited = {}
	solve_recursive(matrix,kings_positions,True,counter,configuration_visited,0)
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

