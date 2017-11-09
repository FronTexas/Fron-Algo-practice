class Solution(object):
	def computeAliveNeighbors(self,board,i,j,m,n):
		alive_neighbors = 0
		neigbor_iterator = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,-1),(1,1),(-1,1)]
		adder_adapter = {
			0:0,
			1:1,
			-1:1,
			2:0
		}
		for iterator in neigbor_iterator:
			if i + iterator[0] >= m or j + iterator[1] >=n or i + iterator[0] < 0 or j + iterator[1] < 0: continue
			alive_neighbors += adder_adapter[board[i+iterator[0]][j+iterator[1]]]
		return alive_neighbors
	def gameOfLife(self, board):
		m = len(board)
		n = len(board[0])

		for i in range(0,m):
			for j in range(0,n):
				number_of_alive_neighbors = self.computeAliveNeighbors(board,i,j,m,n)
				if (number_of_alive_neighbors < 2 or number_of_alive_neighbors > 3) and board[i][j] == 1: 
					board[i][j] = -1 

				if number_of_alive_neighbors == 3 and board[i][j] == 0:
					board[i][j] = 2 

		final_converter = {
        	0:0,
        	1:1,
        	-1:0,
        	2:1
        }

		for i in range(0,m):
			for j in range(0,n):
				board[i][j] = final_converter[board[i][j]]

