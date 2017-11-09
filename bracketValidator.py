BRACKETS = set(['(','{','[',')','}',']'])
CLOSINGS = set(['}',')',']'])
OPENINGS = set(['(','{','['])
BRACKETS_DICT = {'(':')','{':'}','[':']'}

def isBracketValid(s):
	bracket_stack = []

	for c in s: 
		if c in OPENINGS: 
			bracket_stack.append(c)
		if c in CLOSINGS: 
			if len(bracket_stack) == 0: 
				return False

			if c == BRACKETS_DICT[bracket_stack[-1]]:
				bracket_stack.pop()
			else:
				return False
	return True

print isBracketValid('{ [ ] ( ) }')
print isBracketValid('{ [ ( ] ) }')