class Solution:
    
#     def climbStairs(self, n: int) -> int:
#         if n == 1:
#             return 1
#         if n == 2:
#             return 2
        
#         return self.climbStairs(n-1) + self.climbStairs(n-2)
    
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        dp = [0]*n
        dp[0] = 1
        dp[1] = 2
        print(dp)
        for i in range(2,n):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[-1]
    
        
        