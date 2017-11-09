def binarySearch(arr,n):
	start = 0 
	end = len(arr) - 1 

	while (start <= end):
		mid = start + (end-start)/2
		if arr[mid] == n:
			return n 
		if arr[mid] < n: 
			start = mid + 1
		else: 
			end = mid - 1
	return -1 
print binarySearch([1,3,4,5,6,7,8,9,10],10)