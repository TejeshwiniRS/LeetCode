class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        if n==1:
            return max_profit
        l,r=0,1
        while(l<n and r<n):
            if(prices[l]>prices[r]):
                l+=1
                r+=1
                continue
            while(r<n and prices[l]<=prices[r]):
                max_profit = max(max_profit, prices[r]-prices[l])
                r+=1
            l = r-1
        return max_profit