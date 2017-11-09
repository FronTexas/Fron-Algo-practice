def isRifledOnlyOnce(half1,half2,shufled):
	if len(shufled) != len(half1) + len(half2):
		return False
	i = 0 
	j = 0 
	k = 0 
	while (i<len(shufled) and j<len(half2) and k < len(half1)):
		if (k < len(half1) and shufled[i] != half1[k]) or (j < len(half2) and shufled[i] != half2[j]):
			return False

		while (half1[k] == half2[j] == shuffled[i]):
			i += 1 
			j += 1
			k += 1 

		while ((i<len(shufled) and j < len(half2)) and shufled[i] == half2[j]):
			i += 1 
			j += 1 

		while ((i<len(shuffled) and k <len(half1)) and shuffled[i] == half1[k]):
			i += 1 
			k += 1

	return True

isRifledOnlyOnce()
