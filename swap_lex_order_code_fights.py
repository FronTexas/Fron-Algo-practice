'''
	https://codefights.com/interview-practice/task/5vXzdE9yzjsoMZ9sk

	Solution: 
		- Create a union between every single "connected" pair 
		- For each index in the connected pair union, grab str[index], combine them, and sort it decreasing 
		- combine each "combined" string 
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
				i, j = pair
				next_string = swap(i, j, current_string)
				if next_string not in considered_strings:
					stack.append(next_string)
					# string_with_maximum_lex = max(string_with_maximum_lex, next_string)
	return string_with_maximum_lex

def swap(i, j, string):
	modified_string = [c for c in string]
	modified_string[i], modified_string[j] = modified_string[j], modified_string[i]
	return ''.join(modified_string)
 
print swapLexOrder('abdc', [[1, 4], [3, 4]])
print swapLexOrder('a', [])

