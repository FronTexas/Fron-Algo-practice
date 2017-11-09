def findMaxCost(b):
	dp = [[0] * (len(b)),[0] * (len(b))]
	i = 0
	prev = None

	for num in b:
		if prev: 
			d1 = abs(num - prev)
			d2 = abs(num - 1)
			dp[0][i] = max(d1 + dp[0][i-1],d2 + dp[1][i-1])
			
			_d1 = abs(1 - prev)

			dp[1][i] = max(_d1 + dp[0][i-1],dp[1][i-1])
		i+=1
		prev = num

	return max(dp[0][-1],dp[1][-1])

print findMaxCost([10,1,10,1,10])
print findMaxCost([2,1,3,4,5])