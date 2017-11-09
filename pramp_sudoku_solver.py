'''
  1. Every row has 1-9 exactly once
  2. Every col has 1-9 exactly once
  3. Every 3x3 sub-board has 1-9 exactly once 
  
  x x x x x x x x x
  x x x x x x x x x
  x x x x x x x x x
  x x x x x x x x x
  x x x x x x x x x
  x x x x x x x x x
  x x x x x x x x x
  x x x x x x x x x
  x x x x x x x x x
  
  # rns
  row_number_set = {
    i : {1 2 ....}
  }
  
  #cns
  col_number_set = {
  
  }
  
  #sms
  sub_matrix_set = {
    0 : -> 0th sub matrix 
  }
  
  //////////
  
  (i,j) -> 
  
  0th sub_matrix : (-> 
  1st sub_matrix: (0,3) : (2,5)
  .
  .
  .
  7th sub_matrix: (2,1) 
  
  
  (0,1) -> i j
  
  i = 8 
  8 / 3 = 2
  
  j = 3
  3 / 3 = 1
  
  (i,j) = (8,3) = (2, 1)
  
  2 * (# matrixes in a row) + 1
  
  3*i + j 
  
  7
  
  i = 3 
  j = 2 
  
  (3,2) => (1, 0) => 1 * 3 = 3th
  
  
  
  //////////
  
  (i,j) -> 
    
    row i , col j 
    for _n in range(1,9):
      
      if _n not in rns[i] and _n not in cns[i] and _n not in sas[]:
        
    
    check which number that is not in the row yet
    check whcih number that is not in the col yet
    
    
    check whcih number that is not in the 3x3 sub matrix
    
  # rns
  row_number_set = {
    i : {1 2 ....}
  }
  
  #cns
  col_number_set = {
  
  }
  
  #sms
  sub_matrix_set = {
    0 : -> 0th sub matrix 
  }
  

'''

def isValidNumber(i,j,n,rns,cns,sms):
  _i,_j = i/3,j/3
  rnsc = n not in rns[i]
  cnsc = n not in cns[j]
  smsc = n not in sms[3*_i + _j]
  return rnsc and cnsc and smsc


def buildRns(board):
  rns = {}  
  for i in range(len(board)):
    for j in range(len(board)):
      if i in rns: 
        if board[i][j] != '.':
          rns[i].add(int(board[i][j]))
      else: 
        rns[i] = set([])
        if board[i][j] != '.':
          rns[i].add(int(board[i][j]))
  return rns 

def buildCns(board):
  cns = {}  
  for i in range(len(board)):
    for j in range(len(board)):
      if j in cns: 
        if board[i][j] != '.':
          cns[j].add(int(board[i][j]))
      else: 
        cns[j] = set([])
        if board[i][j] != '.':
          cns[j].add(int(board[i][j]))
  return cns 

def buildSms(board):
  sms = {}
  for i in range(len(board)):
    for j in range(len(board)):
        _i , _j = i/3 , j/3 
        key = 3*_i + _j
        if key in sms: 
          if board[i][j] != '.':
            sms[key].add(int(board[i][j]))
        else: 
          sms[key] = set([])
          if board[i][j] != '.':
            sms[key].add(int(board[i][j]))
  return sms


def addNumToDicts(i,j,num,rns,cns,sms):
  rns[i].add(num)
  cns[j].add(num)
  sms_i,sms_j = i/3,j/3
  sms[3*sms_i + sms_j].add(num)


def removeNumFromDicts(i,j,num,rns,cns,sms):
  rns[i].discard(num)
  cns[j].discard(num)
  sms_i,sms_j = i/3,j/3
  sms[3*sms_i + sms_j].discard(num)

def sudoku_solver_recursive(positions,pos_index,rns,cns,sms):
  if pos_index == len(positions):
    return True 
  i,j = positions[pos_index]
  for poss_num in range(1,10):
    if isValidNumber(i,j,poss_num,rns,cns,sms):
      addNumToDicts(i,j,poss_num,rns,cns,sms)
      if sudoku_solver_recursive(positions,pos_index + 1, rns,cns,sms):
        return True 
      removeNumFromDicts(i,j,poss_num,rns,cns,sms)
  return False 


def sudoku_solve(board):
  positions = []
  for i in range(len(board)):
    for j in range(len(board)):
      if board[i][j] == '.':
        positions.append((i,j))

  rns = buildRns(board)
  cns = buildCns(board)
  sms = buildSms(board)
  
  return sudoku_solver_recursive(positions,0,rns,cns,sms)

# ---------------------------


board = [[".","8","9",".","4",".","6",".","5"],[".","7",".",".",".","8",".","4","1"],["5","6",".","9",".",".",".",".","8"],[".",".",".","7",".","5",".","9","."],[".","9",".","4",".","1",".","5","."],[".","3",".","9",".","6",".","1","."],["8",".",".",".",".",".",".",".","7"],[".","2",".","8",".",".",".","6","."],[".",".","6",".","7",".",".","8","."]]
# board = [[".",".",".","7",".",".","3",".","1"],["3",".",".","9",".",".",".",".","."],[".","4",".","3","1",".","2",".","."],[".","6",".","4",".",".","5",".","."],[".",".",".",".",".",".",".",".","."],[".",".","1",".",".","8",".","4","."],[".",".","6",".","2","1",".","5","."],[".",".",".",".",".","9",".",".","8"],["8",".","5",".",".","4",".",".","."]]

def printBoard(board):
  for i in range (len(board)):
    print board[i]

def printDictionaries(dict):
  for key in dict: 
    print dict[key]

printBoard(board)
print 'rns = '
rns = buildRns(board)
printDictionaries(buildRns(board))

print "cns = " 
cns = buildCns(board)
printDictionaries(buildCns(board))

print "sms = "
sms = buildSms(board)
printDictionaries(buildSms(board))

print sudoku_solve(board)

        
            


  
