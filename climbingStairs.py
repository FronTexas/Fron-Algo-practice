def climbingStairs(n):
    dp = [0] * n+1
    if n >= 0:
        dp[0] = 1
    
    for i in range(1,n):
        if i-2 >=0:
            dp[i] = dp[i-2] + 1 
    return dp[-1]

