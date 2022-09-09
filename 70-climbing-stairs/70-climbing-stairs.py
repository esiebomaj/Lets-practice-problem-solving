class Solution:
    
#     def climbStairs(self, n: int) -> int:
#         memo = {}
#         def dfs(n):
#             if n == 0:
#                 return 0
#             if n == 1:
#                 return 1
#             if n == 2:
#                 return 2
            
#             if n in memo:
#                 return memo[n]
            
#             rt = self.climbStairs(n-1) + self.climbStairs(n-2)
            
#             memo[n] = rt
#             return rt
        
#         return dfs(n)
            
    
#     def climbStairs(self, n: int) -> int:
#         if n == 1:
#             return 1
#         if n == 2:
#             return 2
        
#         dp = [0]*n
#         dp[0] = 1
#         dp[1] = 2
        
#         for i in range(2,n):
#             dp[i] = dp[i-1] + dp[i-2]
        
#         return dp[-1]


    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        a,b = 1,2

        for i in range(2,n):
            a,b = b,a+b

        return b
    
        
        