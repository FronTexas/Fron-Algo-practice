def solve_dp(s,p):
       dp = [[False for i in range(len(p))] for j in range(len(s))]
       dp[0][0] = True
       for i in range(len(s)):
              for j in range(len(p)):
                     if withinRange(i-1,j-1,dp) and isMatch(s[i],p[j]):
                                   dp[i][j] = dp[i-1][j-1]
                     if p[j][-1] == '*':
                            if withinRange(i-1,j,dp) and s[i] == p[j][0] or p[j][0] == '.':
                                   dp[i][j] = dp[i][j] or dp[i-1][j]
                            if withinRange(i,j-1,dp) :
                                   dp[i][j] = dp[i][j] or dp[i][j-1]
       return dp[-1][-1]

def solve(i,j,s,p):
       if i == len(s) and j == len(p):
              return True 
       if j < len(p):
              if i < len(s)  and isMatch(s[i],p[j]):
                     if solve(i+1,j+1,s,p): return True
                     if p[j][-1] == '*' and solve(i+1,j,s,p): return True
              if p[j][-1] == '*':
                     if solve(i,j+1,s,p): return True
       return False 

def regularExpressionMatching(s, p):
       p = customSplit(p)
       p = [' '] + p
       s = ' ' + s
       return solve_dp(s,p)

def regularExpressionMatchingRecursive(s, p):
       p = customSplit(p)
       return solve(0,0,s,p)

def customSplit(p):
       out = []
       splitted = p
       i = 0
       while i < len(splitted): 
              if i + 1 < len(splitted) and splitted[i+1] == '*':
                     out.append(splitted[i] + splitted[i+1])
                     i+=2
              else: 
                     out.append(splitted[i])
                     i+=1
       return out

def isMatch(a,b):
       return a == b or b == '.' or a == b[0] or b[0] == '.'


def debug(i,j,s,p):
       print '-------------'
       print 'i = ' + str(i)
       print 'j = ' + str(j)
       if i < len(s): 
              print 's[i] = ' + str(s[i])

       if i == len(s):
              print 's[i] = ' + 'end'

       if j < len(p):
              print 'p[j] = ' + str(p[j])

def withinRange(i,j,dp):
       return 0 <= i and i < len(dp) and 0 <= j and j < len(dp[i])

def print2dMatrix(m):
       for i in range(len(m)):
              print m[i]



def test(actual,expected):
       if expected != actual:
              print '***FAILED***'
              print 'expected = ' + str(expected)
              print 'actual = ' + str(actual)
       print 'PASSED'

def _test(actual,expected,s,p):
       if expected != actual:
              print '***FAILED***'
              print 's = ' + str(s)
              print 'p = ' + str(p)
              print 'expected = ' + str(expected)
              print 'actual = ' + str(actual)
       else:
              print 'PASSED'

s = 'aaaaaaaa'
p = 'a*'
_test(regularExpressionMatching(s,p),True,s,p)

s = 'zabcdcd'
p = 'z.*'
_test(regularExpressionMatching(s,p),True,s,p)


s = 'baaaaaaaa'
p = 'a*'
_test(regularExpressionMatching(s,p),regularExpressionMatchingRecursive(s,p),s,p)

s = 'aaaaax'
p = 'xxxxxxxa.*x'
_test(regularExpressionMatching(s,p),False,s,p)

s = 'a'
p = 'ab*'
_test(regularExpressionMatching(s,p),True,s,p)

s = 'ab'
p = '.*..c*'
_test(regularExpressionMatching(s,p),True,s,p)

# test(customSplit('d*x*a*b'),['d*','x*','a*','b'])