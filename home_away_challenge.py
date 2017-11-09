def countOperations(w):
	i = 0 
	count = 0
	while i < len(w):
		if i + 1 < len(w) and w[i] == w[i+1]:
			count += 1 
			i += 2 
		else: 
			i += 1
	return count


def  minimalOperations(words):
    output = []
	for w in words: 
		output.append(countOperations(w))
    return output

def test(actual,expected):
	if actual != expected: 
		print 'actual = ' + str(actual)
		print 'expected = ' + str(expected)
		print 'FAILED!'
	else: 
		print 'pass'

test(countOperations('aaaaa'),2)
test(countOperations('abcaa'),1)
test(countOperations('abaaaba'),1)
