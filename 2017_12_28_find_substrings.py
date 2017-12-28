class KMP:
	def partial(self, pattern):
		""" Calculate partial match table: String -> [Int]"""
		ret = [0]
		
		for i in range(1, len(pattern)):
			j = ret[i - 1]
			while j > 0 and pattern[j] != pattern[i]:
				j = ret[j - 1]
			ret.append(j + 1 if pattern[j] == pattern[i] else j)
		return ret
		
	def has_match(self, T, P):
		partial, ret, j = self.partial(P), [], 0
		
		for i in range(len(T)):
			while j > 0 and T[i] != P[j]:
				j = partial[j - 1]
			if T[i] == P[j]: j += 1
			if j == len(P): 
				return (True, i - (j - 1))
				j = 0
		return (False, -2)

def insert_at(i, w, c):
	return w[:i] + c + w[i:]

def findSubstrings(words, parts):
	kmp = KMP()
	answer = []

	for word in words: 
		longest_match_so_far = ''
		index_of_longest_match_so_far = len(parts)
		for part in parts: 
			has_match, index_of_match = kmp.has_match(word, part)
			if has_match:
				if len(part) == len(longest_match_so_far) and index_of_match < index_of_longest_match_so_far:
					longest_match_so_far = part
					index_of_longest_match_so_far = index_of_match
				elif len(part) > len(longest_match_so_far):
					longest_match_so_far = part
					index_of_longest_match_so_far = index_of_match
		if len(longest_match_so_far) > 0: 
			modified_word = word 
			modified_word = insert_at(index_of_longest_match_so_far, modified_word, "[")
			modified_word = insert_at(index_of_longest_match_so_far + len(longest_match_so_far) + 1, modified_word, "]")
			answer.append(modified_word)
		else: 
			answer.append(word)
	return answer
	