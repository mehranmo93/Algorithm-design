class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        i = 0
        j = 1
        s = 0
        while j < n:
           # Check each pair of consecutive numbers and take those where the difference is positive

            if prices[j] > prices[i]:
                s1 = prices[j] - prices[i]
                s += s1
            i += 1
            j +=1
        return s


        
            


