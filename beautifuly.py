def isOdd(n):
    return n % 2 != 0

def  beautifulSubarrays(a, m):
    dp = [0 for i in range(len(a))]
    dp[0] = 1
    ans = 0
    odd_counter = 0
    for i in range(1,len(dp)):
        if isOdd(a[i]):
            if odd_counter + 1 > m: 
                ans += 1
                odd_counter = m 
                dp[i] = 1
            elif odd_counter + 1 == m: 
                ans += dp[i-1]
                odd_counter += 1 
                if odd_counter == 1: dp[i] = 1
                dp[i] += dp[i-1]
            else: 
                odd_counter += 1
                if odd_counter == 1: dp[i] = 1
                dp[i] += dp[i-1]
        else: 
            if odd_counter == m: 
                ans += dp[i-1]
                dp[i] = dp[i-1]
            else: 
                dp[i] = dp[i-1]
    print 'dp = ' + str(dp)
    return ans



def  __beautifulSubarrays(a, m):
    dp = [0 for i in range(len(a))]
    dp[0] = 1
    answer = 0
    odd_counter = 0
    for i in range(1,len(dp)):
        if isOdd(a[i]):
            if odd_counter + 1 == m:
                answer += dp[i-1]
                odd_counter = 1 
                dp[i] = dp[i-1]
            else:
                odd_counter += 1
                dp[i] = dp[i-1] + 1
        else: 
            dp[i] = dp[i-1]
    return answer

def  _beautifulSubarrays(a, m):
    dp = [0 for i in range(len(a))]
    dp[0] = 1
    answer = 0
    odd_counter = 0
    for i in range(1,len(dp)):
        if odd_counter == m: 
                answer += dp[i-1]
        if isOdd(a[i]):
            if odd_counter + 1 > m:
                odd_counter = 0
            if odd_counter + 1 == m:
                answer += dp[i-1]
                dp[i] = dp[i-1]
            else:
                dp[i] = dp[i-1] + 1
            odd_counter += 1
        else: 
            dp[i] = dp[i-1]
    return answer

def countOdds(a):
    return sum([1 if isOdd(e) else 0 for e in a ])

def bruteForce(a,m):
    answer = 0
    for i in range(len(a)):
        for j in range(i,len(a)):
            if countOdds(a[i:j+1]) == m:
                answer += 1
    return answer

def test(actual,expected,_input):
    print 'input = ' + str(_input)
    if actual != expected:
        print '** FAILED **'
        print 'actual = ' + str(actual)
        print 'expected = ' + str(expected)
    else: 
        print 'actual = ' + str(actual)
        print 'PASSED'
    print '----'

a = [2,5,4,9]
m = 2
test(beautifulSubarrays(a,m),bruteForce(a,m),(a,m))

a = [2,5,4,9]
m = 3
test(beautifulSubarrays(a,m),bruteForce(a,m),(a,m))

a = [2,5,4,9,11]
m = 2
test(beautifulSubarrays(a,m),bruteForce(a,m),(a,m))

a = [2,5,4,9,2,2,2,2,2,2,2,2,2,2,2,11,13]
m = 2
test(beautifulSubarrays(a,m),bruteForce(a,m),(a,m))

a = [2,5,4,9]
m = 1
test(beautifulSubarrays(a,m),bruteForce(a,m),(a,m))






        
       
                
                
