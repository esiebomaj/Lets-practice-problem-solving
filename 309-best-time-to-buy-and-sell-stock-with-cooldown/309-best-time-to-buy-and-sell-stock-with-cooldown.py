class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}
        
        # dfs + memoization
        # honestly this is the best solution that came out from my brain 
        # it works but quite slow and consumes space
        
        def dfs(i, bought):
            
            if (i, bought) in memo:
                return memo[(i, bought)]
            
            if i >= len(prices):
                return 0 
            
            cool = dfs(i+1, bought)
            
            if bought:
                # we sell or # we dont sell
                sell = dfs(i+2,  False) + prices[i]
                rt = max(sell, cool)
            
            else:
                # we buy or # we dont buy
                buy = dfs(i+1, True) - prices[i]
                rt = max(buy, cool)
            
            memo[(i, bought)] = rt
            return rt
        
        
        return dfs(0,False)