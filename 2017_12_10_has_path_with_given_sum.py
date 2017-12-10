#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def hasPathWithGivenSum(t, s):
	if t == None and s == 0: return True
	if t == None and s != 0: return False

	stack = [(t, t.value)]

	while len(stack) > 0: 
		current_node, current_value = stack.pop()

		if current_node.left == None and current_node.right == None and current_value == s:
			return True 

		if current_node.left != None:
			stack.append((current_node.left, current_value + current_node.left.value))

		if current_node.right != None: 
			stack.append((current_node.right, current_value + current_node.right.value))
	return False
