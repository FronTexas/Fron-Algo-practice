
def krakenCount(m,n):
	matrix= [[0 for i in range(n)] for j in range(m)]
	for i in range(0,m):
		matrix[i][n-1] = 1 
	for j in range(0,n):
		matrix[m-1][j] = 1

	for i in range(m-2,-1,-1):
		iterators = [(1,0),(0,1),(1,1)]
		for j in range(n-2,-1,-1):
			for iterator in iterators:
				add_i,add_j = iterator
				matrix[i][j] += matrix[i+add_i][j+add_j]
	return matrix[0][0]

print krakenCount(100,100)