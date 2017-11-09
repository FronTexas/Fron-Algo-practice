def find2ndLargestElementInBinarySearchTree(node):
	parent = None 
	largest = node 

	while largest.right: 
		parent = largest 
		largest = largest.right 

	if largest.left: 
		temp = largest.left 
		while temp.right: 
			temp = temp.right 
		return temp
	return parent 

