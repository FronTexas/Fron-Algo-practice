# Complete the function below.

def  beautifulSubarrays(a, m):
    dp = [0 for i in range(len(a))]
    odd_number_counter = 0
    if a[0] % 2 != 0: 
        odd_number_counter = 1
    dp[0] = 1
    answer = 0
    for i in range(1,len(dp)):
        if a[i] % 2 != 0:
            odd_number_counter += 1
            if odd_number_counter == m:
                answer += dp[i-1]
                odd_number_counter = 1
                dp[i] = 1
            else:
                dp[i] = dp[i-1] + 1
        else:
            dp[i] = dp[i-1]
    print dp 
    return answer

        
       
                
                
