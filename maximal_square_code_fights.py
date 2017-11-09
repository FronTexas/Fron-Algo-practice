def isValidIndex(matrix,i,j):
    return 0<=i and i < len(matrix) and 0<=j and j < len(matrix[i])

def follows_prev_top_left(matrix,i,j):
    return isValidIndex(matrix,i-1,j-1) and matrix[i-1][j-1] == '1' and isValidIndex(matrix,i-1,j) and matrix[i-1][j] == '1' and isValidIndex(matrix,i,j-1) and matrix[i][j-1] == '1'

def printAt(current_i,current_j,i,j,current,h,l,square_height,square_length,cell_matrix,x,y):
    if current_i == i and current_j ==j:
        print '------------'
        print '(i,j) = ' + str((i,j))
        print 'current_top_left = ' + str(current['top_left'])
        print 'x,y = ' + str((x,y))
        print 'h = ' + str(h)
        print 'l = ' + str(l)
        print 'square_height = ' + str(square_height)
        print 'square_length = ' + str(square_length)

def maximalSquare(matrix):
    cell_matrix = [[{'top_left':(0,0),'length':0,'height':0} for i in range(len(matrix[0]))] for j in range(len(matrix))]
    max_answer = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            current = cell_matrix[i][j]
            if matrix[i][j] == '1':
                current['length'] = 1
                current['height'] = 1 
                
                l = cell_matrix[i][j-1]['length'] if isValidIndex(matrix,i,j-1) else 0 
                h = cell_matrix[i-1][j]['height'] if isValidIndex(matrix,i-1,j) else 0


                x,y = cell_matrix[i-1][j-1]['top_left'] if isValidIndex(matrix,i-1,j-1) and matrix[i-1][j-1] == '1' else (i,j)

                current['top_left'] = (max(i-h,x), max(j-l,y))
                current_x,current_y = current['top_left']

                square_height = i - current_x + 1
                square_length = j - current_y + 1

                if square_length == square_height:
                    max_answer = max(max_answer,square_length * square_height)
                
                current['length'] += l
                current['height'] += h

    return max_answer
              

matrix = [
 ['1','0','1','0','0'], 
 ['1','0','1','1','1'], 
 ['1','1','1','1','1'], 
 ['1','0','0','1','0']
]
print maximalSquare(matrix)