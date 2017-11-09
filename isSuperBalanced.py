def isSuperBalanced(node):
	_min,_max,isBalanced = getminMax(node,0)
	return isBalanced

def isLeaf(node):
	return not node.right and not node.left

def isBalanceIterative(node):
	maxHeight = -sys.maxint - 1 
	minHeight = sys.maxint

	stack = [(node,0)]

	while len(stock) > 0: 
		current,currentHeight = stack[-1]
		del stack[-1]

		if maxHeight - currentHeight > 1 or currentHeight - minHeight > 1: 
			return False

		if current.right: stack.append(current.right,currentHeight + 1)
		if current.left : stack.append(current.left, currentHeight + 1)

		if isLeaf(current): 
			minHeight = min(minHeight,currentHeight)
			maxHeight = max(maxHeight,currentHeight)

			if maxHeight - minHeight > 1: 
				return False
	return True


def getminMax(node,currentHeight):
	if not node.left and not node.right: 
		return (currentHeight,currentHeight,True)

	minLeft , minRight = sys.maxint
	maxLeft , maxRight = -sys.maxint - 1

	if node.left: 
		minLeft,maxLeft,isBalanced = getminMax(node.left,currentHeight + 1)
		if not isBalanced or maxLeft - minLeft > 1:
			return (0,0,False) 

	if node.right: 
		minRight, maxRight, isBalanced = getminMax(node.right,currentHeight + 1)
		if not isBalanced or maxRight - minRight > 1:
			return (0,0,False)

	_min = min(minLeft,minRight)
	_max = max(maxLeft,maxRight)

	if _max - _min > 1: 
		return (0,0,False)

	return _min,_max,True

def checkDepth(node):
	if not node: 
		return 0 

	leftDepth = checkDepth(node['left'])
	if not leftDepth['isBalanced']:
		return {'depth':0,'isBalanced':False}

	rightDepth = checkDepth(node['right'])

	if not rightDepth['isBalanced']:
		return {'depth':0,'isBalanced':False}

	if abs(leftDepth['depth'] - rightDepth['depth']) > 1:
		return {'depth':0,'isBalanced':False}

	return {'depth':max(leftDepth['depth'],rightDepth['depth']) + 1, 'isBalanced': True}


