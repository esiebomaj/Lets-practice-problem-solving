class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # first thing thst comes to mind is to check that the sum divide by 2 is an whole number
        # else we can just return false immidiately
        if sum(nums)%2 != 0:
            return False
        
        # the division by 2 becomes our target 
        # if we can make this target then we can return true
        target = sum(nums)//2
        
        # using a brute force dfs method to check all the posible combinations
        def dfs(i,currSum):
            
            if currSum == target:
                return True
            if currSum > target or i >= len(nums):
                return False
            
            return dfs(i+1, currSum+nums[i]) or dfs(i+1, currSum)
           
        
        return dfs(0, 0)
    
    def canPartition(self, nums: List[int]) -> bool:
        # same idea as the first solution 
        # but this time using memoization in our dfs to reduce repeated computations
        
        if sum(nums)%2 != 0:
            return False
        
        target = sum(nums)//2
        
        memo = {}
        def dfs(i,currSum):
            if (i,currSum) in memo:
                return memo[(i,currSum)]
            
            if currSum == target:
                return True
            if currSum > target or i >= len(nums):
                return False
            
            
            rt = dfs(i+1, currSum+nums[i]) or dfs(i+1, currSum)
            
            memo[(i,currSum)] = rt
            
            return rt
        
        return dfs(0, 0)
            
        
        