'''
	https://codefights.com/interview-practice/task/5vXzdE9yzjsoMZ9sk

	Solution: 
		- Create a union between every single "connected" pair 
		- For each index in the connected pair union, grab str[index], combine them, and sort it decreasing 
		- combine each "combined" string 
'''

def swapLexOrder(str, pairs):
	pairs = [[i-1, j-1] for i, j in pairs]
	connected_pairs = build_connected_pairs(pairs)

def build_connected_pairs(pairs):
	connected_pairs = []
	for pair in pairs: 
		next_connected_pair = build_connected_pairs_starting_from_the_given_pair(pair, pairs, set([]))
		if len(next_connected_pair) > 0: connected_pairs.append(sorted(next_connected_pair))
	return connected_pairs

def build_connected_pairs_starting_from_the_given_pair(starting_pair, pairs, considered_pair):
	stack = [starting_pair]
	connected_pair_so_far = []
	while len(stack) > 0: 
		current_pair = stack.pop()
		
		if tuple(current_pair) in considered_pair: continue
		
		connected_pair_so_far = build_union_of_lists(connected_pair_so_far, current_pair)
		considered_pair.add(tuple(current_pair))

		populate_the_stack_with_connected_pairs(connected_pair_so_far, pairs, considered_pair, stack)

	return connected_pair_so_far

def build_highest_lexes(s, connected_pair):
	_s = [s[index] for index in connected_pair]
	return ''.join(sorted(_s, reverse = True))

def has_connection(list1, list2):
	return len(list(set(list1) & set(list2))) > 0 

def build_union_of_lists(list1, list2):
	return list(set(list1) | set(list2))

def populate_the_stack_with_connected_pairs(connected_pair_so_far, pairs, considered_pair, stack):
	for pair in pairs: 
		if tuple(pair) in considered_pair: continue
		if has_connection(pair, connected_pair_so_far):
			stack.append(pair)

def assertExpectedEqualsActual(test_name, expected, actual): 
	if expected != actual: 
		print '*** FAILED ***'
		print test_name
		print 'expected = ', expected 
		print 'actual = ', actual

assertExpectedEqualsActual('build_connected_pairs',[[1,3,4]], build_connected_pairs([[1, 4], [3, 4]]))
assertExpectedEqualsActual('build_connected_pairs',[[1,3,4,5], [7, 9], [10, 13]], build_connected_pairs([[1, 4], [3, 4], [3,5], [7, 9], [10, 13]]))
assertExpectedEqualsActual('build_highest_lexes', 'dca', build_highest_lexes('abdc', [0, 2, 3]))
assertExpectedEqualsActual('swapLexOrder', 'dbca', swapLexOrder('abdc', [[1, 4], [3, 4]]))
assertExpectedEqualsActual('swapLexOrder', 'a', swapLexOrder('a', []))


