def is_match(text, pattern):
  dp = [[False for i in range(len(text) + 1)] for j in range(len(pattern) + 1)]

  for j in range(len(pattern) + 1):
    for i in range(len(text) + 1):
      if j == 0 and i == 0: 
        dp[j][i] = True 
      else:
        t = text[i-1] if i != 0 else ''
        p = pattern[j-1] if j != 0 else ''

        if t == p or p == '.':
          dp[j][i] = dp[j-1][i-1]
        elif p == '*':
           dp[j][i] = dp[j-2][i] # Check if having zero counts of cp will still results in a match 
           dp[j][i] = dp[j][i] or (pattern[j-2] == t or pattern[j-2] == '.') and dp[j-2][j-2]
  return dp[-1][-1]


print is_match('abbdbb','ab*d'), False
print is_match("aba","a.a") , True 
print is_match("acd","ab*c.") , True 
print is_match("abaa","a.*a*") , True
print is_match("","a*"), True
print is_match('caab','d*x*a*b')