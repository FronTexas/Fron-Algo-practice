# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

def reverse_k_nodes_and_return_head_and_tail(node, k):
	number_of_reversal_left = k - 1
	prev_node = None
	current_node = node 
	head = None
	while current_node:
		next_node = current_node.next

		current_node.next = prev_node

		if number_of_reversal_left == k - 1: 
			tail = current_node 

		if number_of_reversal_left == 1: 
			head = next_node
			break

		nexter_node = next_node.next
		next_node.next = current_node

		prev_node = next_node
		current_node = nexter_node

		number_of_reversal_left -= 1
	tail.next = next_node

	return head, tail


def reverseNodesInKGroups(l, k):


