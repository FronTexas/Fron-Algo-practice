#!/bin/python

import sys

def withinRange(x,y,m):
    return 0 <= x and x < len(m) and 0 <= y and y < len(m[x])

def goHorizontal(m,w,begin,end,constant,visited,iterator = 1):
    for variable in range(begin,end,iterator):
        if not withinRange(constant,variable,m) or (constant,variable) in visited: continue
        m[constant][variable] += w
        visited.add((constant,variable))

def goVertical(m,w,begin,end,constant,visited,iterator = 1):
    for variable in range(begin,end,iterator):
        if not withinRange(variable,constant,m) or (variable,constant) in visited: continue
        m[variable][constant] += w
        visited.add((variable,constant))  

def fill_matrix(m,x,y,w,size_of_square,visited):
    if w == 0: return 
    
    goHorizontal(m,w,y,y+size_of_square,x,visited)
    goVertical(m,w,x,x+size_of_square,y+size_of_square-1,visited)
    goHorizontal(m,w,y+size_of_square-1,y-1,x+size_of_square-1,visited,-1)
    goVertical(m,w,x+size_of_square-1,x-1,y,visited,-1)
    
    if withinRange(x-1,y-1,m):
        fill_matrix(m,x-1,y-1,w-1,size_of_square + 2,visited) 
    elif withinRange(x,y-1,m):
        fill_matrix(m,x,y-1,w -1,size_of_square + 1,visited) 
    elif withinRange(x-1,y,m):
        fill_matrix(m,x-1,y,w-1,size_of_square + 1,visited) 
    

if __name__ == "__main__":
    n = int(raw_input().strip())
    m = int(raw_input().strip())
    matrix = [[0 for i in range(n)] for j in range(n)]
    for a0 in xrange(m):
        x, y, w = raw_input().strip().split(' ')
        x, y, w = [int(x), int(y), int(w)]
        fill_matrix(matrix,x,y,w,1,set([]))
   
    max_w = 0 
    for i in range(len(matrix)):
        #print matrix[i]
        for j in range(len(matrix[i])):
            max_w = max(max_w,matrix[i][j])
    print max_w
        

