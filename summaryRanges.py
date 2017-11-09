class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        b = 0 
        e = b+1 
        answer = []
        while(b < len(nums)):
        	while(e<len(nums) and nums[e] - nums[e-1] == 1):
        		e+=1 
        	if(e-1 < len(nums) and e-1 != b):
        		answer.append(str(nums[b]) + "->" + str(nums[e-1]))
        	else:
        		answer.append(str(nums[b]))

        	b = e
        	e = b+1

        return answer

sol = Solution()
print sol.summaryRanges([0,1,2,4,5,7])