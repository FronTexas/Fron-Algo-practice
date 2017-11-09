class Solution: 
	def checkSubarraySum(self,a,k):
		if(len(a) == 1): 
			return False

		mod_set = set([0])
		if k!= 0: 
			mod_set.add(a[0] % k)
		running_sum = a[0]
		for i in range(1,len(a)):
			e = a[i]
			running_sum += e 
			if k!= 0: running_sum %= k
			if running_sum in mod_set:
				return True
			mod_set.add(running_sum)
		return False

sol = Solution()
print sol.checkSubarraySum([1,2,3],6)