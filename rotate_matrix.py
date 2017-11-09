def switch(a,pos1,pos2):
	i1,j1 = pos1 
	i2,j2 = pos2 
	a[i1][j1],a[i2][j2] = a[i2][j2],a[i1][j1]

def reverse(a,start,end):
	while start < end: 
		a[start],a[end] = a[end],a[start]
		start += 1 
		end -= 1
# accepts the top left coordinate, and the length of the matrix
def rotate(a,i,j,length):
	adder = 1 
	while adder < length - 1:
		switch(a,(i,j+adder),(i+adder,j+length-1))
		adder += 1
	reverse(a[i],j+1,j+length-2)

	adder = 1 
	while adder < length - 1: 
		switch(a,(i,j+adder),(i + length - 1,j + adder))
		adder += 1

	adder = 1 
	while adder < length - 1:
		switch(a,(i,j+adder),(i+adder,j))
		adder += 1
	reverse(a[i],j+1,j+length-2)

	switch(a,(i,j),(i,j + length - 1))
	switch(a,(i,j),(i + length - 1,j + length - 1))
	switch(a,(i,j),(i + length - 1,j))

def rotateImage(a):
	n = len(a)
	if n%2 == 0:
		i,j = n/2 - 1  , n/2  - 1
	else: 
		i,j = n/2,n/2
	length = 2 if n % 2 == 0 else 1 

	while i >= 0 and j >= 0: 
		rotate(a,i,j,length)
		i -= 1
		j -= 1 
		length += 2

	return a 

def print2d(a):
	for i in range(len(a)):
		print a[i]

# a = [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]
# rotateImage(a)
# print2d(a)

# print '-----'
# a = [[1,2],[3,4]]
# rotateImage(a)
# print2d(a)

# print '-----'
# a = [[1, 2, 3,4],
#  [5, 6,7,8],
#  [9,10,11,12],
#  [13,14,15,16]]
# print2d(a)
# print '-'
# rotateImage(a)
# print2d(a)

# print '-----'
# a = [[1, 2, 3,4,5],
#  [6,7,8,9,10],
#  [11,12,13,14,15],
#  [16,17,18,19,20],
#  [21,22,23,24,25]]
# print2d(a)
# print '-'
# # rotateImage(a)
# rotate(a,0,0,5)
# print2d(a)