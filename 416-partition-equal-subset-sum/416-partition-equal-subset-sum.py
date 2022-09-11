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
    
    def canPartition(self, nums: List[int]) -> bool:
        # same idea as the first solution 
        # but this time using memoization in our dfs to reduce repeated computations
        
        if sum(nums)%2 != 0:
            return False
        
        target = sum(nums)//2
        
        # Now this simplifies to finding if we can make target from nums
        # we can do this with a dp table 
        
        dp = [[False]*(target+1) for i in nums] 
        
        for i in range(target+1):
            dp[0][i] = True if i == nums[0] else False
        
        for i in range(len(nums)):
            dp[i][0] = True
        
        for r in range(1, len(nums)):
            for c in range(1, target+1):
                if c < nums[r]:
                    dp[r][c] = dp[r-1][c]
                else:
                    dp[r][c] = dp[r-1][c] or dp[r-1][c-nums[r]]
                    
        # print(dp)
        return dp[-1][-1]
        
        
    #     [1,2,3,4] 5
    
    #     0,1,2,3,4,5
    # 2   T F T F F F    (amount%coins[0])
    # 3   T F T T F T
    # 1   T T T T T T
    # 4   T T T T T T
        
        
       
        
        # first col is always F (cause we cannot make 0 using atleast 1 of n positve ints)  
        
        # if the amount is less than the current coin we take the up one
        
        # if the amount  is reater or equal to the current coin:
        
        # if the one above it is true then the one under is true too
        # can we make the target with the coins before this coin? if yes the we can make it with this coin too
        # SUMMMARY: dp[r][c] = dp[r-1][c] or dp[r-1][c-nums[r]]
        
        
        
        