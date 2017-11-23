# Definition for singly-linked list:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None


def get_nth_node_after_given_node(node, n):
	current_node = node 
	position = 0 

	while current_node != None and position < n: 
		current_node = current_node.next 
		position += 1 
	return current_node

def rearrangeLastN(l, n):
	if n == 0: return l

	head = l 
	prev_head_iter = None
	head_iter = head 
	tail_iter = get_nth_node_after_given_node(head, n - 1)

	# wants to move the head into the front, which is uneccesary
	if not tail_iter.next : return l 

	while tail_iter.next != None: 
		prev_head_iter = head_iter
		head_iter = head_iter.next 
		tail_iter = tail_iter.next

	tail_iter.next = head 
	if prev_head_iter: 
		prev_head_iter.next = None 

	return head_iter