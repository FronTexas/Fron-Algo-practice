# https://codefights.com/interview-practice/task/rMe9ypPJkXgk3MHhZ

class uniqueSum: 
	def __init__(self):
		self.unique_sum = set()
	
	def build_all_possible_sum(self, coin_to_quantity):
		self.build_all_possible_sum_recursive(0, coin_to_quantity)

	def build_all_possible_sum_recursive(self, sum_so_far, coin_to_quantity):
		for coin in coin_to_quantity:
			if coin_to_quantity[coin] > 0: 
				coin_to_quantity[coin] -= 1
				if sum_so_far + coin > 0:
					self.unique_sum.add(sum_so_far + coin)
				self.build_all_possible_sum_recursive(sum_so_far + coin, coin_to_quantity)
				coin_to_quantity[coin] += 1

	def get(self):
		return self.unique_sum



def possibleSums(coins, quantity):
	coin_to_quantity = {coins[i] : quantity[i] for i in range(len(coins))}
	unique_sum = uniqueSum()
	unique_sum.build_all_possible_sum(coin_to_quantity)
	return len(unique_sum.get())

print possibleSums([10,50,100],[1,2,1])