class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}
        
        def dfs(i, cooling, bought, j):
            
            if (i, cooling, bought, j) in memo:
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
    
    
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         # State: Buying or Selling?
#         # If Buy -> i + 1
#         # If Sell -> i + 2

#         dp = {}  # key=(i, buying) val=max_profit

#         def dfs(i, buying):
#             if i >= len(prices):
#                 return 0
#             if (i, buying) in dp:
#                 return dp[(i, buying)]

#             cooldown = dfs(i + 1, buying)
#             if buying:
#                 buy = dfs(i + 1, not buying) - prices[i]
#                 dp[(i, buying)] = max(buy, cooldown)
#             else:
#                 sell = dfs(i + 2, not buying) + prices[i]
#                 dp[(i, buying)] = max(sell, cooldown)
#             return dp[(i, buying)]

#         return dfs(0, True)
        
        
        
        