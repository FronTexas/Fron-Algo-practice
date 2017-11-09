def change_possibilities(goal,coins):
    dp = [0] * (goal + 1)
    dp[0] = 1
    for current_coin in coins:
        for j in range(current_coin,goal + 1):
            if j-current_coin >= 0: 
                dp[j] += dp[j - current_coin]
    return dp[-1]

print change_possibilities(5  ,[5])
print change_possibilities(100  ,[2,3,4])


