def mapDecoding(message):
    dp = [0 for i in range(0,len(message))]
    
    for i,c in enumerate(message): 
        if i == 0:
            dp[i] = 1 
            continue 
        comb = int(message[i-1] + c)
        dp[i] = dp[i-1] + 1 if 0 <= comb and comb <= 26 else dp[i-1]
    return dp[-1]

print mapDecoding("127")