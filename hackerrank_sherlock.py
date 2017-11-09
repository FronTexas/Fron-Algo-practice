def solve(b):
	dp = [[0 for i in range(len(b))] for j in range(2)]
	for i in range(1,len(b)):
		dp[0][i] = max(abs(1-1) + dp[0][i-1],abs(1-b[i-1]) + dp[1][i-1])
		dp[1][i] = max(abs(b[i]-1) + dp[0][i-1],abs(b[i]-b[i-1]) + dp[1][i-1])
	return max(dp[0][-1],dp[1][-1])


t = int(raw_input())
for _t in range(t):
    n = int(raw_input())
    b = [int(e) for e in raw_input().split(' ')]
    print solve(b)