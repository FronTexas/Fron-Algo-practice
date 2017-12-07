# https://codefights.com/interview-practice/task/rMe9ypPJkXgk3MHhZ


'''
	Approach: 
		Function signature f(sum_so_far, unique_sum_set, coins)

		do a breadth first iteration through the coins: 
			add each coin to sum_so_far, create new coins with 
			the coin removed, put the coin back to coins, continue breadth first iteration
'''

class Queue: 
	def __init__(self):
		self.arr = []

	def __len__(self):
		return len(self.arr)

	def pop(self):
		if len(self.arr) == 0: return None
		
		to_return = self.arr[0]
		del self.arr[0]

		return to_return

	def append(self, val):
		self.arr = [val] + self.arr

class State: 
	def __init__(self, sum_so_far, coin_to_quantity):
		self.sum_so_far = sum_so_far
		self.coin_to_quantity = coin_to_quantity

class uniqueSum: 



	def __init__(self, coin_to_quantity = {}):
		self.unique_sum = set()
		self.build_all_possible_sum_bfs(coin_to_quantity)
	
	def build_all_possible_sum(self, coin_to_quantity):
		self.build_all_possible_sum_recursive(0, coin_to_quantity)

	def get_decreased_coin_quantity(self, coin_to_quantity, coin_to_decrease):
		modified_coin_to_quantity = {coin : quantity for coin, quantity in coin_to_quantity.iteritems()}
		modified_coin_to_quantity[coin_to_decrease] = modified_coin_to_quantity[coin_to_decrease] - 1
		return modified_coin_to_quantity

	def build_all_possible_sum_bfs(self, coin_to_quantity):
		'''
			The state (coin_to_quantity) and the queue cannot be seperate ??
			OR 
			the queue is a state that contains (coin, sum_so_far, the desired coin_to_quantity)
		'''
		state_queue = Queue()
		state_queue.append(State(0, coin_to_quantity))

		while len(state_queue) > 0: 
			print self.unique_sum
			current_state = state_queue.pop()
			for coin in current_state.coin_to_quantity:
				coin_has_no_quantity = current_state.coin_to_quantity[coin] == 0 
				considered_the_sum_before = current_state.sum_so_far in self.unique_sum
				
				if coin_has_no_quantity: continue
				
				state_queue.append(
					State(
						current_state.sum_so_far + coin, 
						self.get_decreased_coin_quantity(coin_to_quantity, coin)
					)
				)
				self.unique_sum.add(current_state.sum_so_far + coin)

	def build_all_possible_sum_recursive(self, sum_so_far, coin_to_quantity):
		for coin in coin_to_quantity:
			coin_has_no_quantity = coin_to_quantity[coin] == 0
			if coin_has_no_quantity: continue 
			coin_to_quantity[coin] -= 1
			self.unique_sum.add(sum_so_far + coin)
			self.build_all_possible_sum_recursive(sum_so_far + coin, coin_to_quantity)
			coin_to_quantity[coin] += 1

	def get(self):
		return self.unique_sum



def possibleSums(coins, quantity):
	coin_to_quantity = {coins[i] : 0 for i in range(len(coins))}
	for i, coin in enumerate(coins):
		coin_to_quantity[coin] += quantity[i]

	unique_sum = uniqueSum(coin_to_quantity)
	return len(unique_sum.get())

print possibleSums([10,50,100],[1,2,1])
print possibleSums([10, 50, 100, 500], [5, 3, 2, 2])
print possibleSums([1, 1, 1, 1, 1], [9, 19, 18, 12, 19])
print possibleSums([3, 1, 1], [111, 84, 104])