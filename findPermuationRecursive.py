def findPermutation(s,alreadySearchedThis):
	if len(s) == 1: 
		return set([s])

	augmented_permutation = set()
	for i in range(0,len(s)):
		current = s[i]
		nextS = ''.join([s[j] for j in range(0,len(s)) if j!=i])

		if nextS in alreadySearchedThis: 
			augmented_permutation = augmented_permutation.union(set([current + e for e in alreadySearchedThis[nextS]]))

		if nextS not in alreadySearchedThis:
			permutation_from_substring = findPermutation(nextS,alreadySearchedThis)
			alreadySearchedThis[nextS] = permutation_from_substring
			augmented_permutation = augmented_permutation.union(set([current + e for e in permutation_from_substring]))
	return augmented_permutation

# print findPermutation('1',{})


def findPermutation(s):
	if len(s) == 1: 
		return [s]

	augmented_permutation = []
	for i in range(0,len(s)):
		current = s[i]
		nextS = ([s[j] for j in range(0,len(s)) if j!=i])
		permutation_from_substring = findPermutation(nextS)
		augmented_permutation = augmented_permutation + [[current] + e for e in permutation_from_substring]
	return augmented_permutation

findPermutation([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])