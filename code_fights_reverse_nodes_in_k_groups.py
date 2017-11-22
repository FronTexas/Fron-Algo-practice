# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

def has_k_nodes_after_node(node, k):
	current_node = node
	node_counter = 0
	while current_node:
		current_node = current_node.next
		node_counter += 1
		if node_counter == k:
			return True 
	return False


def get_kth_node_after_given_node(node, k):
	current_node = node 
	iteration_count = 0 

	while iteration_count < k:
		current_node = current_node.next
		iteration_count += 1

	return current_node

def reverse_k_nodes_and_return_head_and_tail(node, k):
	# the "first" node will be the new tail
	tail = node

	number_of_reverses_left = k

	current_node = node

	kth_node = get_kth_node_after_given_node(node, k)
	prev = kth_node

	while number_of_reverses_left > 0: 
		next_node = current_node.next
		
		current_node.next = prev
		
		prev = current 
		current = next_node
		
		number_of_reverses_left -= 1
	head = prev 
	return head, tail


def reverseNodesInKGroups(l, k):
	ZEROTH_ITERATION = 0
	current_node = l 
	number_of_iteration = 0
	new_head, prev_tail = None

	while has_k_nodes_after_node(current_node):
		head, tail = reverse_k_nodes_and_return_head_and_tail(current_node, k)
		
		if prev_tail:
			prev_tail.next = head

		if number_of_iteration == ZEROTH_ITERATION: 
			new_head = head 

		prev_tail = tail
		current_node = tail.next
		number_of_iteration += 1
	
	return new_head
