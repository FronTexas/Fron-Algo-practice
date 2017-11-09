def findMaxProfit(prices):
	max_price_so_far = 0
	total_profit = 0
	for i in range(len(prices)-1,-1,-1):
		max_price_so_far = max(prices[i],max_price_so_far)
		total_profit += max_price_so_far - prices[i]
	return total_profit

def test(actual,expected):
	if actual != expected: 
		print 'actual = ' + str(actual)
		print 'expected = ' + str(expected)
		print 'FAILED!'
	else: 
		print 'pass'

test(findMaxProfit([1,2,100,92,90,97,200]),818)
test(findMaxProfit([5,3,2]),0)
test(findMaxProfit([1,2,100]),197)
test(findMaxProfit([1,3,1,2]),3)





