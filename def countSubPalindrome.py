def isPalindrome(s,start,end):
	while start < end: 
		if s[start] != s[end]: return False
		start += 1 
		end -= 1 
	return True


def countSubPalindrome(s,start,end,visited):
	if (start,end) in visited: 
		return 
	visited.add((start,end))
	result = 0 
	if isPalindrome(s,start,end):
		result = 1
	return result + countSubPalindrome(s,start + 1,end,visited) + countSubPalindrome(s,start,end-1)

s = 'hellolle'
print countSubPalindrome(s,0,len(s)-1,set([]))

