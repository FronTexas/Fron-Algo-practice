def possibleSums(coins, quantities):
	possible_sums = set([0])
	for i, coin in enumerate(coins): 
		for j in range(quantities[i]):
			prev_possible_sums = set(possible_sums)
			for possible_sum in prev_possible_sums:
				possible_sums.add(possible_sum + coin)
	return len(possible_sums) - 1

