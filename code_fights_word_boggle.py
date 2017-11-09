'''
    board = [
        [c1 c2 c3 ....]
        .
        .
        .
    ]
    
    words = [w1,w2,w3,.....]
    
    return words that can be formed by iterating the board 
    
    board = [
        ['R', 'L', 'D'],
        ['U', 'O', 'E'],
        ['C', 'S', 'O']
    ]
    
    word = "CODEOSC"
    
    f(char_to_look_for,forbidden_points):
        directions = [(i,j),up,diagonal,down...]
        for dir in directions:
            if (i,j) not in forbidden_points and board(i,j) == char_to_look_for:
                f(next char_to_look_for)
'''

def isValidPoints(board,i,j):
    return 0 <= i and i < len(board) and 0 <= j and j < len(board[i])

def wordBoggleRecursive(board,word,current_coord,index_to_look_for,forbidden_points):
    if index_to_look_for == len(word):
        return True
    directions = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    for _i,_j in directions: 
        i,j = current_coord
        next_i,next_j = i + _i,j + _j
        if isValidPoints(board,next_i,next_j) and (next_i,next_j) not in forbidden_points and board[next_i][next_j] == word[index_to_look_for]:
            forbidden_points.add(current_coord)
            forbidden_points.add((next_i,next_j))
            if(wordBoggleRecursive(board,word,(next_i,next_j),index_to_look_for + 1,forbidden_points)): return True
            forbidden_points.discard(current_coord)
            forbidden_points.discard((next_i,next_j))
    return False 

def findStartingPoints(board,word):
    starting_points = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == word[0]:
                starting_points.append((i,j))
    return starting_points

def wordBoggle(board, words):
    words.sort()
    answers = []
    for word in words: 
        starting_points = findStartingPoints(board,word)
        for starting_point in starting_points: 
            if(wordBoggleRecursive(board,word,starting_point,1,set([]))):
                answers.append(word)
                break;
    return answers

def test(actual,expected):
    print 'actual = ' + str(actual)
    print 'expected = ' + str(expected)
    print actual == expected