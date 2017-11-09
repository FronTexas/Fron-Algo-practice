
def isValidIndex(i,j,m):
  return i >= 0 and i < len(m) and j >= 0 and j < len(m[0])

def traverse_matrix(bm,boolean_matrix,i,j):
  boolean_matrix[i][j] = True
  stack = [(i,j)]
  
  while len(stack) > 0: 
    ci,cj = stack.pop()
    directions = [(ci - 1,cj),(ci,cj+1),(ci + 1,cj),(ci,cj-1)]

    for vi,vj in directions:
      if isValidIndex(vi,vj,bm) and not boolean_matrix[vi][vj]:
        if bm[vi][vj] == 1 : 
          stack.append((vi,vj))
          boolean_matrix[vi][vj] = True 
  
def get_number_of_islands(bm):
  island_counter = 0
  boolean_matrix = [[False for i in range(len(bm[0]))] for j in range(len(bm))]
  for i in range(len(bm)):
    for j in range(len(bm[i])):
      if bm[i][j] == 1 and not boolean_matrix[i][j]: 
        traverse_matrix(bm,boolean_matrix,i,j)
        island_counter += 1
  return island_counter        

bm = [[0,1,0,1,0],[0,0,1,1,1],[1,0,0,1,0],[0,1,1,0,0]]
print get_number_of_islands(bm)

bm = [[1,1,0,0],[1,1,1,0],[0,1,1,0],[0,0,0,1]]
print get_number_of_islands(bm)
