class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [[0]*(amount+1) for coin in range(len(coins)+1)]
        
        for c in range(len(coins)+1):
            dp[c][0] = 1
        
        # r and c stand for row and column
        
        for r in range(1, len(coins)+1):
            for c in range(1, amount+1):
                if c < coins[r-1]:
                    dp[r][c] = dp[r-1][c]
                else:
                    dp[r][c] = dp[r-1][c] + dp[r][c-coins[r-1]]
        # print(dp)
        return dp[-1][-1]
                    
        # 2 options
        # => we use the curr coin +
        # => we dont use the curr coin        
        
#           0,1,2,3,4,5
        
#       .   0 0 0 0 0 0
#       1   1 1 1 1 1 1
#       2   1 1 2 2 3 3
#       5   1 1 2 2 2 4