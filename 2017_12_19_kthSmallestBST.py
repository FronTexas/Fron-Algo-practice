#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def kthSmallestInBST(t, k):
	current = t 
	visit_counter = 0
	while current != None: 
		if current.left == None: 
			visit_counter += 1
			if visit_counter == k:
				return current.value
			current = current.right 
		else: 
			predecessor = find_predecessor(current)
			if predecessor.right == None: 
				predecessor.right = current 
				current = current.left 
			else: 
				predecessor.right = None 
				visit_counter += 1 
				if visit_counter == k: 
					return current.value
				current = current.right
	return None

def find_predecessor(t):
	target = t.value
	current = t.left
	while current and current.right != None and current.right.value != target:
		current = current.right 
	return current

