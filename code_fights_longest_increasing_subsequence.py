def longestIncreasingSubsequence(sequence):
    dp = [1 for i in range(len(sequence))]
    ans = 0 
    for i in range(len(sequence)):
        # i == 3
    	for j in range(i):
            # j = 0 
    		if sequence[j] < sequence[i]:
    			dp[i] = max(dp[i],dp[j] + 1)
		ans = max(ans,dp[i])
    return ans

def test(actual,expected,input):
	if actual != expected:
		print 'actual = ' + str(actual)
		print 'expected = ' + str(expected)
		print 'input = ' + str(input)

# sequence = [1, 231, 2, 4, 89, 32, 12, 234, 33, 90, 34, 100]
# test(longestIncreasingSubsequence(sequence),7,sequence)


'''

arr =               [45, 40, 27, 24, 38, 39, 19, 83, 30, 42, 34, 16, 40, 59]

length_at_index_i = [                                                        ]
                      idx=0 , idx = 1 , ....                            idx=n
                                               ^
                                               i
                      j = 0
'''

sequence = [45, 40, 27, 24, 38, 39, 19, 83, 30, 42, 34, 16, 40, 59]
test(longestIncreasingSubsequence(sequence),5,sequence)
