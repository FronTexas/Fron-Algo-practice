#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def isSubtree(t1, t2):
	if t2 == None: 
		return True

	possible_starts = find_possible_starts(t1, t2)

	for possible_start in possible_starts:
		if found_match(possible_start, t2): return True 
	return False 

def find_possible_starts(t1, t2):
	stack = [t1]
	possible_starts = []
	while len(stack) > 0:
		current = stack.pop()
		if not current: continue
		if current.value == t2.value:
			possible_starts.append(current)
		if current.right != None: stack.append(current.right)
		if current.left != None: stack.append(current.left)
	return possible_starts


def found_match(t1, t2):
	stack1 = [t1]
	stack2 = [t2]

	while len(stack2) > 0: 
		current1 = stack1.pop()
		current2 = stack2.pop()
		if (current1 and current2) and (current1.value != current2.value):
			return False
		if current1 == None and current2 != None:
			return False 
		if current1 != None and current2 == None: 
			return False 

		if current1 != None:
			stack1.append(current1.right)
			stack1.append(current1.left)
		if current2 != None:
			stack2.append(current2.right)
			stack2.append(current2.left)
	return True



