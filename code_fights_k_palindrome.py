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
		Solve the subproblem first, meaning, 
		figure out all the k_scores for every single sub problem and then solve the main problem
		iteration #2:
			Create a 2d matrix where the ith index indicates the index of ith character of s and 
			jth index indicates which character is removed from s 

			(i, j) indicates how many character that if removed can make the string palindrome

		iteration #3
			Come up with all possible 1 character strings, 2 character strings, 3 character strings,....
			and for each n character strings, the solution was built on the previous solution of n-1 character strings. 
			The complexity is still bad since it's gonna be n + n^2 + n^3 + ..... n^n which is still exponential.....

		TODO iteration #4
			Try to solve edit distance algo problem
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
	answer = k_palindrome_helper(s, 0, k, cache)
	print cache['ara']
	return answer


print k_palindrome('abrarbra', 1)
# print k_palindrome('adbcdbacdb', 2)

