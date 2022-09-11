class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {}
        def dfs(i, currSum):
            if (i,currSum) in memo:
                return memo[(i,currSum)]
            if currSum == target and i == len(nums):
                return 1
            if i == len(nums):
                return 0
            
            rt = dfs(i+1, currSum + nums[i]) + dfs(i+1, currSum - nums[i])
            memo[(i, currSum)] = rt
            return rt
            
        return dfs(0,0)
