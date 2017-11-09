def spiral_copy(inputMatrix):
  result = []
  j = 0
  top_row = 0 
  right_col = len(inputMatrix[0])
  left_col = 0 
  bottom_row = len(inputMatrix)
  while(top_row < bottom_row and left_col < right_col): 
    for j in range(left_col,right_col):
      result.append(inputMatrix[top_row][j])
    top_row += 1
    for j in range(top_row,bottom_row):
        result.append(inputMatrix[j][right_col])
    right_col -= 1
    for j in range(right_col,left_col):
         result.append(inputMatrix[bottom_row][j])
    bottom_row -= 1
    for j in range(bottom_row,top_row):
         result.append(inputMatrix[j][left_col])
    left_col += 1

inputMatrix  = [ [1,    2,   3,  4,    5],
                         [6,    7,   8,  9,   10],
                         [11,  12,  13,  14,  15],
                         [16,  17,  18,  19,  20] ]
print spiral_copy(inputMatrix)