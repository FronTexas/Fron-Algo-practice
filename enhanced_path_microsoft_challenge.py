def is_command(s):
	if s == '*':
		return True

	number_of_dots = s.count('.')
	if number_of_dots > 0 and number_of_dots == len(s):
		return True

	return False

def build_answer(stack):
	if len(stack) == 0: 
		return '\\'
	answer = []
	for i,e in enumerate(stack): 
		if i == 0 or i < len(stack):
			answer.append('\\')
		answer.append(str(e))
	return ''.join(answer) 

def test(actual,expected):
	print 'expected = '  + str(expected)
	print 'actual = ' + str(actual)
	print expected == actual

with open('./enhanced_path_input.txt') as f:
	for line in f:
		line_splitted = line.split('\\')

		stack = []

		for e in line_splitted:
			e = e.rstrip()
			if is_command(e):
				if e == '*':
					stack = []
				else:
					for i in range(len(e)): 
						if i != 0 and len(stack) > 0: 
							stack.pop()
			else: 
				stack.append(e)

		# print stack
		answer = build_answer(stack)
		# print 'length = ' + str(len(answer))
		# print 'last is  ' + str(answer[-1] == '\n')
			print answer
