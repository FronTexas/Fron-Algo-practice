def get_highest_product_of_3(numbers):
	nums_that_gives_highest_3 = []
	negative_numbers = []

	for num in numbers: 
		nums_that_gives_highest_3.append(num)
		if len(nums_that_gives_highest_3) > 3:
			nums_that_gives_highest_3 =  sorted(nums_that_gives_highest_3)
			del nums_that_gives_highest_3[0]
		if num < 0: 
			negative_numbers.append(num*-1)
			if len(negative_numbers) > 2: 
				negative_numbers = sorted(negative_numbers)
				del negative_numbers[0]
	
	sorted(nums_that_gives_highest_3)
	sorted(negative_numbers)

	first_two_product = nums_that_gives_highest_3[0] * nums_that_gives_highest_3[1]
	negative_number_product = negative_numbers[0] * negative_numbers[1] if len(negative_numbers) == 2 else 1 

	toReturn = first_two_product * nums_that_gives_highest_3[-1] if first_two_product > negative_number_product else negative_number_product * nums_that_gives_highest_3[-1]
	return toReturn

print get_highest_product_of_3([2,-20,20,37,4,-45])
print get_highest_product_of_3([1,10,-5,1,-100])