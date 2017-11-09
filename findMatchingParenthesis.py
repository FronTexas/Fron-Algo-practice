def findMathcingParenthesis(word,opening_index):
	parenthesis_counter = 1 
	index = opening_index + 1

	while(index < len(word)):
		c = word[index]
		if c == ')':
			parenthesis_counter -= 1 
			if parenthesis_counter == 0: 
				return index
		if c == '(':
			parenthesis_counter += 1 
		index += 1 
	raise Exception("No Closing Parenthesis!")

print findMathcingParenthesis('Sometimes (when I nest them (my parentheticals) too much (like this (and this)) they get confusing.',10)