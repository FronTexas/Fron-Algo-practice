'''
	https://codefights.com/interview-practice/task/AaWaYxi8gjtbqgp2M/description
'''
class BinaryTreeRestorer: 
	def __init__(self):
		self.pre_order_index = 0 

	def restore_binary_tree_recursive(self, start, end):
		if start > end: return 
		current_node = Tree(self.preorder[self.pre_order_index])
		index_of_current_node = self.node_to_inorder_index[current_node.value]
		self.pre_order_index += 1
		current_node.left = self.restore_binary_tree_recursive(start, index_of_current_node - 1)
		current_node.right = self.restore_binary_tree_recursive(index_of_current_node + 1, end)
		return current_node
	
	def restore(self, inorder, preorder):
		self.inorder = inorder
		self.preorder = preorder
		self.node_to_inorder_index = {node : i for (i, node) in enumerate(inorder)}
		return self.restore_binary_tree_recursive(0, len(inorder) - 1)

def restoreBinaryTree(inorder, preorder):
	'''
		traverse through the preorder, each node that we're at, 
		we decide what is the left and right child of that node
	'''
	b = BinaryTreeRestorer()
	return b.restore(inorder, preorder)





