class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ###### more intuitive solution using M*N time and space
#         dp = [[0]*(amount+1) for coin in coins]
        
#         for i in range(len(coins)):
#             dp[i][0] = 0
        
#         for i in range(1, amount+1):
#             dp[0][i] = float(inf) if i%coins[0] != 0 else i//coins[0]
        
        
#         for r in range(1, len(coins)):
#             for c in range(1, amount+1):
#                 coin = coins[r]
#                 if c >= coin:
#                     dp[r][c] = min(dp[r-1][c], dp[r][c-coin]+1)
#                 else:
#                     dp[r][c] = dp[r-1][c]
                    
        
#         return -1 if dp[-1][-1] == float(inf) else dp[-1][-1]



        ### more Efficient solution using M*N time and M space
    
        dp = [0]*(amount+1) 
        
        for i in range(1, amount+1):
            dp[i] = float(inf) if i%coins[0] != 0 else i//coins[0]
                    
        
        for r in range(1, len(coins)):
            for c in range(1, amount+1):
                coin = coins[r]
                if c >= coin:
                    dp[c] = min(dp[c], dp[c-coin]+1)
                    
        
        return -1 if dp[-1] == float(inf) else dp[-1]
    
    
    
    