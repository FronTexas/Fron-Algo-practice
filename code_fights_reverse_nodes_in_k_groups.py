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

	# the tail.next will be the kth_node after node 
	prev = kth_node

	while number_of_reverses_left > 0: 
		next_node = current_node.next
		
		current_node.next = prev
		
		prev = current_node 
		current_node = next_node
		
		number_of_reverses_left -= 1
	head = prev 
	return head, tail


def reverseNodesInKGroups(l, k):
	current_node = l 
	is_first_iteration = True
	new_head = None
	prev_tail = None

	while has_k_nodes_after_node(current_node, k):
		head, tail = reverse_k_nodes_and_return_head_and_tail(current_node, k)
		
		if prev_tail:
			prev_tail.next = head

		if is_first_iteration: 
			is_first_iteration = False
			new_head = head 

		prev_tail = tail
		current_node = tail.next
	
	return new_head
