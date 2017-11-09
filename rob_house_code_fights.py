def houseRobber(nums):
	max_rob = [0 for i in range(0,len(nums))]
	for i in range(0,len(nums)):
		if i == 0: 
			max_rob[i] = nums[i]
		elif i == 1: 
			max_rob[i] = max(max_rob[i-1],nums[i])
		else:
			max_rob[i] = max(max_rob[i-1],nums[i] + max_rob[i-2])  
	return max_rob[-1]

nums = [155, 44, 52, 58, 250, 225, 109, 118, 211, 73, 137, 96, 137, 89, 174, 66, 134, 26, 25, 205, 239, 85, 146, 73, 55, 6, 122, 196, 128, 50, 61, 230, 94, 208, 46, 243, 105, 81, 157, 89, 205, 78, 249, 203, 238, 239, 217, 212, 241, 242, 157, 79, 133, 66, 36, 165]
print houseRobber(nums)