class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1
        
        for r in range(1,len(coins)+1):
            for c in range(1,amount+1):
                coin = coins[r-1]                        
                if coin > c:
                    pass
                else:
                    dp[c] = dp[c] + dp[c-coin]
        
        return dp[-1]
    
#         dp = [[0]*(amount+1) for i in range(len(coins)+1)]
#         for i in range(len(coins)+1):
#             dp[i][0] = 1
        
#         for r in range(1,len(coins)+1):
#             for c in range(1,amount+1):
#                 coin = coins[r-1]                        
#                 if coin > c:
#                     dp[r][c] = dp[r-1][c]
#                 else:
#                     dp[r][c] = dp[r-1][c] + dp[r][c-coin]
        
#         return dp[-1][-1]
    
        
                
                    
"""
    0,1,2,3,4,5
[]  1 0 0 0 0 0
[1] 1 1 1 1 1 1
[2] 1 1 2 2 3 3
[5] 1 1 1 1 1 4

use it + dont use it

dont use it = dp[r-1][c]
use it = dp[r][c-coin] 
"""