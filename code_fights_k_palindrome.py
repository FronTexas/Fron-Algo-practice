'''
https://codefights.com/interview-practice/task/x3rJpdZGEcjmYtDqv

A string is a k-palindrome if it can be transformed into a palindrome 
by removing any amount of characters from 0 to k. 
Your task is to determine whether the given string s is a k-palindrome.

'''
def add(cache, key, value):
	if key in cache: 
		cache[key].add(value)
	else:
		cache[key] = {value}

def remove(s, i):
	return s[:i] + s[i+1:]

def is_palindrome(s):
	start = 0 
	end = len(s) - 1 

	while start < end: 
		if s[start] != s[end]:
			return False 
		start += 1 
		end -= 1 
	return True

def k_palindrome_dp(s):
	'''
		Solve the subproblem first meaning, 
		figure out all the k_scores for every single sub problem and then solve the main problem
	'''

def k_palindrome_helper(s, char_removed, k, cache):
	if s in cache: 
		return k - char_removed in cache[s]
	
	if is_palindrome(s):
		add(cache, s, 0)

	for i, c in enumerate(s):
		next_s = remove(s, i)
		if k_palindrome_helper(next_s, char_removed + 1, k, cache): 
			return True 
		if next_s in cache:
			for k_score in cache[next_s]:
				add(cache, s, k_score + 1)

	return k - char_removed in cache[s]

def k_palindrome(s, k):
	cache = {}
	return k_palindrome_helper(s, 0, k, cache)

print k_palindrome('abrarbra', 1)
print k_palindrome('adbcdbacdb', 2)

