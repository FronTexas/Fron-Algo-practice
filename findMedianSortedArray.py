class Solution(object):
	def findMedianSortedArrays(self,nums1,nums2):
		a = 0
		b = len(nums1) - 1 
		length1 = (b-a) + 1


		ap = 0 
		bp = len(num2)-1
		length2 = (bp-ap) + 1



		md_1 = nums[(b-a)/2] if (length1) % 2 != 0 else nums[length1/2] - nums[(length1/2) - 1]
		md_2 = nums[(bp-a[])/2] if (length2) % 2 != 0 else nums[length2/2] - nums[(length2/2) - 1]

		while():
			if md_1 == md2: 
				return md_1

			if md_1 < md_2: 
				
