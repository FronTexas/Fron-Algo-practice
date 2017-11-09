def decrement(i,numbers):
	numbers[i] -= 1

def increment(i,numbers):
	numbers[i] += 1

def allSame(numbers):
	elm = numbers[0]
	for i in range(len(numbers)):
		if elm != numbers[i]: return False 
	return True 

def countMovesRecursive(numbers,steps,memo):
	if tuple(numbers) in memo: return memo[tuple(numbers)]

	if allSame(numbers): return steps
	min_answer = 2**32
	for i in range(len(numbers)):
		if numbers[i] == 0: continue 
		decrement(i,numbers)
		min_answer = min(countMovesRecursive(numbers,steps + 1,memo),min_answer)
		memo[tuple(numbers)] = min_answer
		increment(i,numbers)
	return min_answer


def countMoves(numbers):
	return countMovesRecursive(numbers,0,{})

print countMoves([5,6,8,8,5])

    

