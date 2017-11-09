RED = 0 
GREEN = 1 
BLUE = 2

def paintHouses(cost):
    dp = [[0,0,0] for i in range(len(cost))]
    dp[0][RED] = cost[0][RED]
    dp[0][GREEN] = cost[0][GREEN]
    dp[0][BLUE] = cost[0][BLUE]
    
    for i in range(1,len(dp)):
        dp[i][RED] = min(dp[i-1][GREEN] + cost[i][RED],dp[i-1][BLUE] + cost[i][RED])
        dp[i][GREEN] = min(dp[i-1][RED] + cost[i][GREEN],dp[i-1][BLUE] + cost[i][GREEN])
        dp[i][BLUE] = min(dp[i-1][RED] + cost[i][BLUE],dp[i-1][GREEN] + cost[i][BLUE])
    
    return min(dp[-1][RED],dp[-1][GREEN],dp[-1][BLUE])

def test(actual,expected,_input):
    if actual != expected: 
        print '**** FAILED ****'
        print 'input = ' + str(_input)
        print 'actual = ' + str(actual)
        print 'expected = ' + str(expected)
    else: 
        print 'VVVV PASSED VVVV'

cost = [[3,6,4], 
 [1,2,8], 
 [2,4,7], 
 [5,10,1], 
 [3,4,3], 
 [6,4,1], 
 [8,7,2], 
 [5,6,1], 
 [6,7,3], 
 [5,10,3]]

test(paintHouses(cost),29,cost)