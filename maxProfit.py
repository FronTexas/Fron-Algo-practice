class Solution(object):
    def maxProfit(self, prices):
        if len(prices) < 2: 
            return 0
        
        max_profit_so_far = prices[1] - prices[0]
        minimum_price_so_far = min(prices[0],prices[1])

        if len(prices) < 3: 
        	if max_profit_so_far > 0:
        		return max_profit_so_far
        	return 0 

        for i in range(2,len(prices)):
        	price = prices[i]
        	max_profit_so_far = max(price - minimum_price_so_far,max_profit_so_far)
        	minimum_price_so_far = min(minimum_price_so_far,price)

        if max_profit_so_far > 0:
        	return max_profit_so_far
        return 0

sol = Solution()
print sol.maxProfit([7, 100])
        