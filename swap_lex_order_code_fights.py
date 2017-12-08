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


def build_connected_pairs_recursive(connected_pair_so_far, pairs, memo, connected_pairs):
	for pair in pairs: 
		if tuple(pair) not in memo and (len(connected_pair_so_far) == 0 or has_connection(connected_pair_so_far, pair)):
			memo.add(tuple(pair))
			build_connected_pairs_recursive(build_union(connected_pair_so_far, pair), pairs, memo, connected_pairs)
	
	if len(connected_pair_so_far) > 0: 
		connected_pairs.append(connected_pair_so_far)

def has_connection(list1, list2):
	return len(list(set(list1) & set(list2))) > 0 

def build_union(list1, list2):
	return list(set(list1) | set(list2))

def build_connected_pairs(pairs):
	connected_pairs = []
	build_connected_pairs_recursive([], pairs, set([]), connected_pairs)
	return connected_pairs

def assertExpectedEqualsActual(test_name, expected, actual): 
	if expected != actual: 
		print '*** FAILED ***'
		print test_name
		print 'expected = ', expected 
		print 'actual = ', actual

print assertExpectedEqualsActual('build_connected_pairs',[[1,3,4]], build_connected_pairs([[1, 4], [3, 4]]))
# print assertExpectedEqualsActual('swapLexOrder', 'dbca', swapLexOrder('abdc', [[1, 4], [3, 4]]))
# print assertExpectedEqualsActual('swapLexOrder', 'a', swapLexOrder('a', []))


