#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

'''
Inorder traversal: [4, 2, 1, 5, 3, 6]
Preorder traversal: [1, 2, 4, 3, 5, 6]

IDEA: 
@ 3, 3 is in the right side of both 1, 2, and 4. But 3's parent has to be 1 because, 
3 is in the right side of 1, and 1 is the most "important" parent 

a1 == [ 1, 2, 4

a2 == 4, 2, 1 ]

@ 1, 1 is the root 

@ 2, is 2 in the left of 1 in the inorder? Yes! -> 2 is the left of 1

// Looking at a2
@ 4, is 4 in the left of 2 in inorder? Yes! -> 4 is the left of 2


/* Anomali */
@ 4, is 4 in the right of 1 in inorder? No! ->  We're dealing the left sub tree of 1
/* Anomali */


/* Anomali */
@ 3, is 3 in the right of 1 in inorder? Yes! -> We're done dealing with the left sub tree of 1, 
entering right sub tree. -> 3 is the right of 1 
/* Anomali */

@ 5, is 5 in the left of 3 in inorder? Yes! -> 5 is the left of 3
@ 6, is 6 in the right of 3 in inorder? -> 6 is the right of 3 

           1 
         2  3
        4  5 6

'''
def restoreBinaryTree(inorder, preorder):
	'''
		traverse through the preorder, each node that we're at, 
		we decide what is the left and right child of that node
	'''
