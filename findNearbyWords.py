def isWord(w):
	return True

def getNearbyChars(c):
	if c == 'g':
		return ['g','h','f']
	else:
		return ['i','o','k']


def findNeearbyWordsHelper(current,index,result,w):
	if index == len(w):
		if isWord(current):
			result.append(current)
		return

	nearby = getNearbyChars(w[index])

	for c in nearby: 
		findNeearbyWordsHelper(current + c, index + 1,result,w)
	return 

def findNearbyWords(w):
	result = []
	findNeearbyWordsHelper('',0,result,w)
	return result


print findNearbyWords('gi')