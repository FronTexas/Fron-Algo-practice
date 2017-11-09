# Complete the function below
def maxDifference(a):
	max_so_far = 10**6 * -1
	ans = 10**6 * -1
	for i in range(len(a)-1,-1,-1):
		max_so_far = max(max_so_far,a[i])
		ans = max(max_so_far-a[i],ans)
	if ans == 0:
		return -1
	return ans

print maxDifference([10,8,7,6,5])
                 
