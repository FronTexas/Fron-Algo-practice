'''
    given n
     
     f(col):
         for row in that col 
          check if row,col is valid 
              place the queen in row,col 
              f(col + 1)
              remove the queen from row,col
    
    x x x x x x .....n 
    x x
    x x
    x x
    x x
    x x  x
    x     x (r,c)
    .
    .
    n
    
    # queens_positions = { row:col }
    queens_positions = {
        1:1,
        3:2,
        .
        .
    }
    
    
    
    [    r  ]
         c
    print all possible distinct solution
'''
def isPositionValid(row,col,n,queens_positions):
    if row in queens_positions:
        return False 
    
    row_iterator = row
    col_iterator = col 
    
    while row_iterator >= 1 and col_iterator >= 1: 
        if row_iterator in queens_positions: 
            if queens_positions[row_iterator] == col_iterator:
                return False 
        row_iterator -= 1
        col_iterator -= 1
    
    row_iterator = row 
    col_iterator = col 
    
    while row_iterator <= n and col_iterator >= 1:
        if row_iterator in queens_positions: 
            if queens_positions[row_iterator] == col_iterator:
                return False 
        row_iterator += 1
        col_iterator -= 1
    return True
    
def nQueensRecursive(col,n,queens_positions,answers):
    if col > n:
        an_answer = [0 for e in range(n)]
        for row,col in queens_positions.iteritems():
            an_answer[col-1] = row 
        answers.append(an_answer)
        return
    for row in range(1,n + 1):
        if isPositionValid(row,col,n,queens_positions):
            queens_positions[row] = col
            nQueensRecursive(col + 1,n,queens_positions,answers)
            del queens_positions[row]

def nQueens(n):
    queens_positions = {}
    answers = []
    nQueensRecursive(1,n,queens_positions,answers)
    return answers

def test(actual,expected):
    print 'actual = ' + str(actual)
    print 'expected = ' + str(expected)
    print actual == expected

n = 4 
expected = [[2, 4, 1, 3],[3, 1, 4, 2]]
test(nQueens(n),expected)

