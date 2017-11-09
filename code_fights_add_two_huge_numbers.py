def addTwoHugeNumbers(a,b):
	a = reverse(a)
	b = reverse(b)

	i = a 
	j = b 
	result = ListNode(None)
	current = result
	carry = 0
	while i or j or carry:
		i_value = 0 
		j_value = 0
		if i: i_value = int(i.value)
		if j: j_value = int(j.value)
		_sum = i_value + j_value + carry
		carry = _sum / 10000 
		presented_sum = _sum if _sum < 10000 else _sum-10000
		current.value = presented_sum 
		
		if (i and i.next) or (j and j.next) or carry > 0: current.next = ListNode(None)
		current = current.next 
		if i: i = i.next 
		if j: j = j.next
	result = reverse(result)
	return result

def reverse(l):
	if not l.next: return l 

	prev = None
	trail = l 
	head = l.next 

	while head: 
		trail.next = prev 
		temp = head.next
		head.next = trail 

		prev = trail
		trail = head
		head = temp 
	return trail


