def knapsack(w,weights,prices):
	m = [[0 for i in range(w+1)] for j in range(len(weights))]

	for i in range(len(m)):
		for j in range(len(m[i])):
			value = m[i][j]
			if i - 1 >= 0:
				value = m[i-1][j]
			weight_left = j - weights[i]
			if weight_left >= 0: 
				total_without_current_weight = m[i-1][weight_left] if i - 1 >= 0 else 0
				value = max(prices[i] + total_without_current_weight , value)

			m[i][j] = value
	print m
	return m[-1][-1]


w = 7 
weights = [1,3,4,5]
prices = [1,4,5,7] 
print knapsack(7,weights,prices)