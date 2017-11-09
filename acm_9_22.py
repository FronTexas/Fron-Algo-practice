def solution_dp(prices,k):
	dp = [0 for i in range(len(prices))]
	curr_max = -1
	for i in range(k):
		curr_max = max(curr_max,prices[i])
		dp[i] = curr_max
	for i in range(k,len(prices)):
		dp[i] = max(prices[i] + dp[i-k],dp[i-1])
	return dp[-1]


def solution_recursive(i,prices,k,memo):
	if i in memo: 
		return memo[i]
	profit = prices[i]
	for j in range(i+k,len(prices)):
		profit = max(prices[i] + solution_recursive(j,prices,k,memo),profit)
		memo[i] = profit
	return profit

def solution(prices,k):
	profit = 0
	memo = {}
	for i in range(0,len(prices)):
		profit = max(solution_recursive(i,prices,k,memo),profit)
	return profit

def test(expected,actual):
	if expected != actual:
		print 'expected = ' + str(expected)
		print 'actual = ' + str(actual)
		print '****FAILED****'
	else: 
		print 'Passed'


n,k = [int(e) for e in raw_input().strip().split(' ')]
prices = [int(e) for e in raw_input().strip().split(' ')]
print solution(prices,k)
print solution_dp(prices,k)

