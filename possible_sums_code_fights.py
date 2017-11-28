# https://codefights.com/interview-practice/task/rMe9ypPJkXgk3MHhZ

def possibleSumRecursive(unique_sum, sum_so_far, coin_to_quantity):
	if sum_so_far > 0:
		unique_sum.add(sum_so_far)
	for coin in coin_to_quantity:
		if coin_to_quantity[coin] > 0: 
			coin_to_quantity[coin] -= 1
			possibleSumRecursive( unique_sum, sum_so_far + coin, coin_to_quantity)
			coin_to_quantity[coin] += 1




def possibleSums(coins, quantity):
	coin_to_quantity = {coins[i] : quantity[i] for i in range(len(coins))}
	unique_sum = set()
	possibleSumRecursive(unique_sum, 0, coin_to_quantity)
	return len(unique_sum)

print possibleSums([10,50,100],[1,2,1])