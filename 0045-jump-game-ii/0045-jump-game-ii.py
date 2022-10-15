class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i):
            
            if i in memo:
                return memo[i]
            
            if i >= len(nums)-1:
                return 0
            
            rt = float(inf)
            for j in range(1, nums[i]+1):
                rt = min(rt, dfs(i+j)+1)
            
            memo[(i)] = rt
            return rt
        
        return dfs(0)
        