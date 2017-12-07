'''
	https://codefights.com/interview-practice/task/5vXzdE9yzjsoMZ9sk
'''

def swapLexOrder(str, pairs):
	considered_strings = set([])
	stack = [str]
	string_with_maximum_lex = str
	pairs = [[i-1, j-1] for i, j in pairs]

	while len(stack) > 0: 
		current_string = stack.pop()
		if current_string not in considered_strings:
			considered_strings.add(current_string)
			for pair in pairs: 
				next_string = swap(pair, current_string)
				stack.append(next_string)
				string_with_maximum_lex = max(string_with_maximum_lex, next_string)
	return string_with_maximum_lex

def swap(pair, string):
	i, j = pair
	modified_string = [c for c in string]
	modified_string[i], modified_string[j] = modified_string[j], modified_string[i]
	return ''.join(modified_string)

print swapLexOrder('abdc', [[1, 4], [3, 4]])
