class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
##### More intuitive solution using m by n time and space
##### Understand this soution first before moving to the second one
        
#         dp = [[0]*(amount+1) for coin in range(len(coins)+1)]
        
#         for c in range(len(coins)+1):
#             dp[c][0] = 1
        
#         # r and c stand for row and column
#         for r in range(1, len(coins)+1):
#             for c in range(1, amount+1):
#                 if c < coins[r-1]:
#                     dp[r][c] = dp[r-1][c]
#                 else:
#                     dp[r][c] = dp[r-1][c] + dp[r][c-coins[r-1]]

#         return dp[-1][-1]



##### Optimized soltion using M*N time but M space

        dp = [0]*(amount+1)
        
        dp[0] = 1
        
        # r and c stand for row and column
        
        for r in range(1, len(coins)+1):
            for c in range(1, amount+1):
                if c < coins[r-1]:
                    pass
                else:
                    dp[c] += dp[c-coins[r-1]]

        return dp[-1]
                    
        # 2 options
        # => we use the curr coin +  we dont use the curr coin        