class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}
        
        def dfs(i, cooling, bought, j):
            
            if (i, cooling, bought, j) in memo:
                # print("returning from memo", (i, cooling, bought, j))
                return memo[(i, cooling, bought, j)]
            
            if i == len(prices):
                return 0 
            
            if cooling:
                # we wait
                rt = dfs(i+1, False, bought, j)
            
            elif bought != False:
                # we sell or # we dont sell
                rt = max(dfs(i+1, True, False, 0)+(prices[i]-j), dfs(i+1, False, bought, j))
            
            else:
                # we buy or # we dont buy
                rt = max(dfs(i+1, False, True, prices[i]), dfs(i+1, False, bought, j))
            
            memo[(i, cooling, bought, j)] = rt
            return rt
        
        
        return dfs(0,False,False,0)
        
        
        
        