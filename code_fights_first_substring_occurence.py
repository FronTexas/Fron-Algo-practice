def computeLPS(x):
	lps = [0 for i in range(0,len(x))]
	i = 1 
	length = 0 
	while i < len(x):
		if x[i] == x[length]:
			length += 1 
			lps[i] = length 
			i += 1 
		else: 
			if length != 0: 
				length = lps[length-1]
			else: 
				length = 0 
				i+=1 
	return lps


def findFirstSubstringOccurrence(s,x):
	lps = computeLPS(x)

	i = 0 
	j = 0 

	while i < len(s):
		if s[i] == x[j]:
			i+=1 
			j+=1
		if j == len(x):
			return i-j
		elif i < len(s) and s[i] != x[j]:
			if j > 0: 
				j = lps[j-1]
			else: 
				i+= 1
	return -1



print computeLPS('AAACAAAAAC')

