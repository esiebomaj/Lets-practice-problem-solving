class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}
        
        # dfs + memoization
        # honestly this is the best solution that came out from my brain 
        # it works but quite slow and consumes space
        
        def dfs(i, bought, j):
            
            if (i, bought, j) in memo:
                return memo[(i, bought, j)]
            
            if i >= len(prices):
                return 0 
            
            
            if bought:
                # we sell or # we dont sell
                rt = max(dfs(i+2,  False, 0)+(prices[i]-j), dfs(i+1, bought, j))
            
            else:
                # we buy or # we dont buy
                rt = max(dfs(i+1, True, prices[i]), dfs(i+1, bought, j))
            
            memo[(i, bought, j)] = rt
            return rt
        
        
        return dfs(0,False,0)