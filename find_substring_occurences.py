def build_lps(a):
    i = 0 
    j = 1 
    lps = [0 for c in a]
    while(j<len(a)):
        if a[i] == a[j]:
            lps[j] = lps[j-1] + 1
            i+=1 
        else: 
            if a[0] == a[j]: 
                lps[j] = lps[j-1]
            else:
                lps[j] = 0 
                i = 0 
        j+=1 
    return lps


def findFirstSubstringOccurrence(s, x):
    lps = build_lps(x)
    i = 0 
    j = 0 

    while(i < len(s)):
        while(s[i] == x[j]): 

        j = lps[j-1]

           
        
# s = 'afafafafaafafafaf'
# x = 'afafafaafa'
# print findFirstSubstringOccurrence(s,x)

print build_lps('abababca');
print build_lps('AABAACAABAA');
print build_lps('AAACAAAA');
print computeLPSArray('AAACAAAA',len('AAACAAAA'))