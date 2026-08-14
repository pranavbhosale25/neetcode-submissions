class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices) 
        if l == 1 or l == 0:
            return 0

        if l == 2 and prices[0] > prices[1]: # no profit
            return 0

        maxProfit = 0
        left = 0
        right = 1

        while left < l and right < l:
            if prices[right] < prices[left]:
                left = right
                right = left + 1
                continue
            else:
                maxProfit = max(maxProfit, prices[right]-prices[left])
                right += 1
                print(maxProfit)

        return maxProfit
