class Solution:

	def findClosestHigherElement(self,target,nums,begin):
		j = len(nums) - 1
		while(j>=begin and nums[j] <= target){
			j-=1
		}
		return j

	def reverse(self,nums,begin):
		left = begin 
		right = len(nums) - 1

		while left < right: 
			nums[left],nums[right] = nums[right],nums[left]
			left += 1 
			right -= 1 

	def partition(self,a,begin,end):
		pivot = begin 
		for i in range(begin+1,end+1):
			if(a[i] <= a[begin]):
				pivot += 1 
				a[pivot],a[i] = a[i],a[pivot]
		
		a[begin],a[pivot] = a[pivot],a[begin]
		return pivot

	def _sort(self,nums,begin,end):
		if begin >= end:
			return
		partition_index = self.partition(nums,begin,end)
		self._sort(nums,begin,partition_index-1)
		self._sort(nums,partition_index + 1,end)

	def nextPermutation(self,nums):
		right = len(nums) - 1 
		left = right - 1

		while(left >= 0 and nums[left] >= nums[right]):
			right = left 
			left = right - 1
		
		if left < 0: 
			self.reverse(nums,0)
			return

		smallest_after_left_index = self.findClosestHigherElement(nums[left],nums,left + 1)

		nums[left],nums[smallest_after_left_index] = nums[smallest_after_left_index],nums[left]

		self._sort(nums,left+1,len(nums)-1)
		# self.reverse(nums,left+1)
	

sol = Solution()	
nums = [int(c) for c in '6987']
print 'input = ' + str(nums)
sol.nextPermutation(nums)
print 'output = ' + str(nums)

nums = [2,1,2,2,2,2,2,1]
print 'input = ' + str(nums)
sol.nextPermutation(nums)
print 'output = ' + str(nums)

nums = [2,3,1,3,3]
print 'input = ' + str(nums)
sol.nextPermutation(nums)
print 'output = ' + str(nums)

nums = [int(c) for c in '231']
print 'input = ' + str(nums)
sol.nextPermutation(nums)
print 'output = ' + str(nums)

nums = [int(c) for c in '312']
print 'input = ' + str(nums)
sol.nextPermutation(nums)
print 'output = ' + str(nums)
