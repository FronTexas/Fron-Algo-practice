class Solution(object):

    def wordBreak(self,s,words):
        d = [False] * len(s)
        for i in range(0,len(d)):
            for w in words:
                if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w)+1 == 0):
                    d[i] = True 
        return d[-1]

    def wordBreakHelper(self,s,begin,wb,w_d):
        for i in range(begin,len(s)):
            wb += s[i]
            if wb in w_d:
                if i == len(s) - 1: return True
                if(self.wordBreakHelper(s,i+1,'',w_d)): return True
        return False 
    
    def word_Break(self, s, wordDict):
        return self.wordBreakHelper(s,0,'',set(wordDict))   

sol = Solution()
print sol.wordBreak('leetcode',['le','et','etco','de']);
        
        
        