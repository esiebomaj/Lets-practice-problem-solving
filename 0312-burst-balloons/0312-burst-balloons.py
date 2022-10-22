class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1]+nums+[1]
        memo = {}
        def dfs(l,r):
            
            if l > r:
                return 0
            
            if (l,r) in memo:
                return memo[(l,r)]
            
            res = float(-inf)
            for i in range(l, r+1):
                ans = (nums[i]*nums[l-1]*nums[r+1]) + dfs(l,i-1) + dfs(i+1,r)
                res = max(res, ans)
            memo[(l,r)] = res
            return res
        
        return dfs(1,len(nums)-2)
                
                
            
        















# class Solution:
#     def maxCoins(self, nums: List[int]) -> int:
        
#         def burst(ballons, i):
#             res = ballons[i]
#             if i > 0: 
#                 res *= ballons[i-1]
                
#             if i < len(ballons)-1:
#                 res *= ballons[i+1]
                
#             newBallons = ballons.copy()
#             newBallons.pop(i)
                
#             return res, newBallons
                
            
        
#         def dfs(ballons):
#             if len(ballons) == 0:
#                 return 0
            
#             rt = float(-inf)
#             for i,p in enumerate(ballons):
                
#                 amount, newBallons = burst(ballons, i)
#                 rt = max(rt, amount + dfs(newBallons))
            
#             return rt
        
#         return dfs(nums)
            
                
                
                
        