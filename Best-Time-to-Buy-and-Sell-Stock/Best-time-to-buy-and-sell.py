class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = float('inf')  # Initialize minPrice to infinity
        maxProfit = 0  # Initialize maxProfit to 0
        
        for price in prices:
            if price < minPrice:
                minPrice = price 
            elif price - minPrice > maxProfit:
                maxProfit = price - minPrice       
        return maxProfit