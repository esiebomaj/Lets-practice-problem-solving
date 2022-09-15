class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}
        
        def dfs(i):
            if i in memo:
                return memo[i]
            
            if i >= len(nums)-1:
                memo[i] = 0
                return 0
            
            jumps = float(inf)
            for j in range(1, nums[i]+1):
                res = dfs(i+j)
                jumps = min(jumps, res+1)
            
            memo[i] = jumps
            return jumps
                
        return dfs(0)
                
[2,3,1,1,4]