class Solution(object):
	def findTargetSumWays(self,nums,t):
		_sum = sum(nums)

		if (t+_sum) % 2 != 0 or _sum < t: return 0 

		p = (t + _sum) >> 1
		dp = [0] * (p+1)
		dp[0] = 1
		for n in nums: 
			for i in range(p,n-1,-1):
				dp[i] += dp[i-n]

		return dp[-1]

sol = Solution()
print sol.findTargetSumWays([1, 1, 1, 1, 1],3)