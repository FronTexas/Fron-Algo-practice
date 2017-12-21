#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def restoreBinaryTree(inorder, preorder):
	'''
		traverse through the preorder, each node that we're at, 
		we decide what is the left and right child of that node
	'''