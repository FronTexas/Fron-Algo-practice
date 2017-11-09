
MAX = 'MAX'
MIN = 'MIN'


def isValidBinarySearchTree(node):
	s = [(node,-float("inf"),float("inf"))]

	while len(s):
		node, lowerBound, upperBound = s.pop()

		if node.data < lowerBound or node.data > upperBound:
			return False 

		if node.left: 
			s.append((node.left,lowerBound,node.data))
		if node.right: 
			s.append((node.right,node.data,upperBound))

	return True


def isValidBinarySearchTree(node,lookingFor):
	if(node):
		current = node.value 

		_max,isValid = isValidBinarySearchTree(node.left,MAX)

		if not isValid or(_max and _max >= current): 
			return (None,False)

		_min,isValid = isValidBinarySearchTree(node.right,MIN)

		if not isValid or (_min and _min <= current):
			return (None,False)

		if lookingFor == MAX:
			if _min:
				return (max(current,_min,_max),True)
			return (current,True)

		if lookingFor = MIN:
			if _max:
				return(min(current,_max,_min),True)
			return(current,True)
	return (None,True)