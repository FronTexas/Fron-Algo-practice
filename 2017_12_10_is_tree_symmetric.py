#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def isTreeSymmetric(t):
	if t == None: return True
	if left(t) != right(t): return False 

	stack = [(t.left, t.right)]

	while len(stack) > 0: 
		left_node, right_node = stack.pop()

		if left(left_node) != right(right_node) or right(left_node) != left(right_node): return False 

		if left_node.left and right_node.right:
			stack.append((left_node.left, right_node.right))
		if left_node.right and right_node.left:
			stack.append((left_node.right, right_node.left))
	
	return True

def left(t):
	if t == None: return None
	if t.left == None: return None
	return t.left.value

def right(t): 
	if t == None: return None
	if t.right == None: return None 
	return t.right.value

